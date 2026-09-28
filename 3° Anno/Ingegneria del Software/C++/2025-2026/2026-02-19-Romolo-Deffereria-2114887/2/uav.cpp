#include "uav.hpp"
#include <cmath>

UAV::UAV(int id, double V, double T, double L, int Q) 
    : V(V), T(T), L(L), Q(Q) {
    (void)id;
}

void UAV::init(std::mt19937& gen) {
    std::uniform_real_distribution<double> dist_pos(-L, L);
    x[0] = dist_pos(gen);
    x[1] = dist_pos(gen);
    x[2] = dist_pos(gen);
}

void UAV::update(std::mt19937& gen, const std::vector<std::vector<double> >& all_positions) {
    double max_d = -1.0;
    std::vector<std::pair<double, double> > best_angles;

    const double PI = std::acos(-1.0);

    for (int q_theta = 0; q_theta <= Q; ++q_theta) {
        double theta = (static_cast<double>(q_theta) / Q) * PI;
        for (int q_phi = 0; q_phi <= Q; ++q_phi) {
            double phi = (static_cast<double>(q_phi) / Q) * 2.0 * PI;

            double v1 = V * std::sin(theta) * std::cos(phi);
            double v2 = V * std::sin(theta) * std::sin(phi);
            double v3 = V * std::cos(theta);

            double z[3] = {
                x[0] + v1 * T,
                x[1] + v2 * T,
                x[2] + v3 * T
            };

            double d_val = 0;
            for (const auto& pos : all_positions) {
                for (int k = 0; k < 3; ++k) {
                    double diff = (z[k] - pos[k]) / (2.0 * L);
                    d_val += diff * diff;
                }
            }

            // Using a small epsilon for floating point comparison
            if (best_angles.empty() || d_val > max_d + 1e-9) {
                max_d = d_val;
                best_angles.clear();
                best_angles.push_back(std::make_pair(theta, phi));
            } else if (std::abs(d_val - max_d) <= 1e-9) {
                best_angles.push_back(std::make_pair(theta, phi));
            }
        }
    }

    double best_theta, best_phi;
    if (best_angles.size() > 1) {
        std::uniform_int_distribution<int> dist(0, best_angles.size() - 1);
        int idx = dist(gen);
        best_theta = best_angles[idx].first;
        best_phi = best_angles[idx].second;
    } else {
        best_theta = best_angles[0].first;
        best_phi = best_angles[0].second;
    }

    double v1 = V * std::sin(best_theta) * std::cos(best_phi);
    double v2 = V * std::sin(best_theta) * std::sin(best_phi);
    double v3 = V * std::cos(best_theta);

    x[0] += v1 * T;
    x[1] += v2 * T;
    x[2] += v3 * T;
}

std::vector<double> UAV::getPosition() const {
    std::vector<double> pos;
    pos.push_back(x[0]);
    pos.push_back(x[1]);
    pos.push_back(x[2]);
    return pos;
}

void UAV::setPosition(const std::vector<double>& new_pos) {
    x[0] = new_pos[0];
    x[1] = new_pos[1];
    x[2] = new_pos[2];
}
