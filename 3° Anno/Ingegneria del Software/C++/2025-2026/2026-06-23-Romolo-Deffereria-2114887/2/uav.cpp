#include "uav.hpp"
#include "network.hpp"
#include <cmath>
#include <limits>
#include <vector>
#include <utility>

UAV::UAV(int id, Network* net, double L, std::mt19937& gen) : id(id), net(net) {
    std::uniform_real_distribution<double> dist_pos(-L, L);
    for (int k = 0; k < 3; ++k) {
        x[k] = dist_pos(gen);
        z[k] = dist_pos(gen); // target
    }
    const double PI = std::acos(-1.0);
    std::uniform_real_distribution<double> dist_theta(0.0, PI);
    std::uniform_real_distribution<double> dist_phi(0.0, 2.0 * PI);
    theta = dist_theta(gen);
    phi = dist_phi(gen);
}

double UAV::distance_to_target() const {
    double dist_sq = 0.0;
    for (int k = 0; k < 3; ++k) {
        double diff = x[k] - z[k];
        dist_sq += diff * diff;
    }
    return std::sqrt(dist_sq);
}

void UAV::step(double V, double T, double a, double b, double r, double A, double B, std::mt19937& gen) {
    // Current velocity v(t)
    double v1_t = V * std::sin(theta) * std::cos(phi);
    double v2_t = V * std::sin(theta) * std::sin(phi);
    double v3_t = V * std::cos(theta);

    // Position at t+1
    double x1[3];
    x1[0] = x[0] + T * v1_t;
    x1[1] = x[1] + T * v2_t;
    x1[2] = x[2] + T * v3_t;

    // Step 1: Find neighbors within distance r at time t
    const auto& uavs = net->get_uavs();
    std::vector<int> neighbors;
    for (int j = 0; j < (int)uavs.size(); ++j) {
        if (j == id) continue; // id is 0-indexed, same as index in uavs
        const double* xj = uavs[j]->get_position();
        double dist_sq = 0;
        for (int k = 0; k < 3; ++k) {
            double diff = x[k] - xj[k];
            dist_sq += diff * diff;
        }
        if (std::sqrt(dist_sq) <= r) {
            neighbors.push_back(j);
        }
    }

    double best_J = std::numeric_limits<double>::max();
    std::vector<std::pair<int, int> > best_choices;

    // Evaluate all 9 combinations of (u, w)
    for (int u_val = -1; u_val <= 1; ++u_val) {
        for (int w_val = -1; w_val <= 1; ++w_val) {
            // Angles at t+1
            double theta1 = theta + T * a * u_val;
            double phi1 = phi + T * b * w_val;

            // Velocity at t+1
            double v1_t1 = V * std::sin(theta1) * std::cos(phi1);
            double v2_t1 = V * std::sin(theta1) * std::sin(phi1);
            double v3_t1 = V * std::cos(theta1);

            // Position at t+2
            double x2[3];
            x2[0] = x1[0] + T * v1_t1;
            x2[1] = x1[1] + T * v2_t1;
            x2[2] = x1[2] + T * v3_t1;

            // distance to target at t+2
            double d_target_sq = 0.0;
            for (int k = 0; k < 3; ++k) {
                double diff = x2[k] - z[k];
                d_target_sq += diff * diff;
            }
            double d_target = std::sqrt(d_target_sq);

            // F(t+2, i): min distance to current neighbors (assumed stationary)
            double F_val = 0.0;
            if (!neighbors.empty()) {
                F_val = std::numeric_limits<double>::max();
                for (int j : neighbors) {
                    const double* xn = uavs[j]->get_position();
                    double dist_sq = 0;
                    for (int k = 0; k < 3; ++k) {
                        double diff = x2[k] - xn[k];
                        dist_sq += diff * diff;
                    }
                    double d_n = std::sqrt(dist_sq);
                    if (d_n < F_val) F_val = d_n;
                }
            }

            // Objective J = A * d_target - B * F_val
            // We want to minimize J
            double J_val = A * d_target - B * F_val;

            if (best_choices.empty() || J_val < best_J - 1e-9) {
                best_J = J_val;
                best_choices.clear();
                best_choices.push_back(std::make_pair(u_val, w_val));
            } else if (std::abs(J_val - best_J) <= 1e-9) {
                best_choices.push_back(std::make_pair(u_val, w_val));
            }
        }
    }

    // Choose one optimal (u, w) uniformly at random
    int chosen_u, chosen_w;
    if (best_choices.size() == 1) {
        chosen_u = best_choices[0].first;
        chosen_w = best_choices[0].second;
    } else {
        std::uniform_int_distribution<int> dist_idx(0, best_choices.size() - 1);
        int idx = dist_idx(gen);
        chosen_u = best_choices[idx].first;
        chosen_w = best_choices[idx].second;
    }

    // Update state to t+1
    x[0] = x1[0];
    x[1] = x1[1];
    x[2] = x1[2];

    theta += T * a * chosen_u;
    phi += T * b * chosen_w;
}
