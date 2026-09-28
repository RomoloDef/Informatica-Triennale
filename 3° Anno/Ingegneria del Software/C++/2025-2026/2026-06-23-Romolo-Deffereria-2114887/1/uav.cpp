#include "uav.hpp"
#include <cmath>
#include <limits>
#include <vector>
#include <utility>

UAV::UAV(double L, std::mt19937& gen) {
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

void UAV::step(double V, double T, double a, double b, std::mt19937& gen) {
    // Current velocity v(t)
    double v1_t = V * std::sin(theta) * std::cos(phi);
    double v2_t = V * std::sin(theta) * std::sin(phi);
    double v3_t = V * std::cos(theta);

    // Position at t+1
    double x1[3];
    x1[0] = x[0] + T * v1_t;
    x1[1] = x[1] + T * v2_t;
    x1[2] = x[2] + T * v3_t;

    double best_dist = std::numeric_limits<double>::max();
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

            // Distance to target at t+2
            double dist_sq = 0.0;
            for (int k = 0; k < 3; ++k) {
                double diff = x2[k] - z[k];
                dist_sq += diff * diff;
            }
            double dist = std::sqrt(dist_sq);

            if (best_choices.empty() || dist < best_dist - 1e-9) {
                best_dist = dist;
                best_choices.clear();
                best_choices.push_back(std::make_pair(u_val, w_val));
            } else if (std::abs(dist - best_dist) <= 1e-9) {
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
