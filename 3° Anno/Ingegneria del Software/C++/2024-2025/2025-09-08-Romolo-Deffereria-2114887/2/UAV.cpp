#include "UAV.hpp"
#include <cmath>
#include <algorithm>
#include <limits>

UAV::UAV(double init_x1, double init_x2, double init_x3) {
    x[0] = init_x1;
    x[1] = init_x2;
    x[2] = init_x3;
}

void UAV::update_and_move(double T, double V, double A, double L, const std::vector<std::unique_ptr<UAV>>& all_uavs, std::mt19937& gen) {
    std::uniform_real_distribution<double> dis_p(0.0, 1.0);
    double v[3];
    
    for (int k = 0; k < 3; ++k) {
        double p = std::exp(-A * (x[k] + L) / (2.0 * L));
        if (dis_p(gen) < p) {
            v[k] = V;
        } else {
            v[k] = -V;
        }
    }
    
    for (int k = 0; k < 3; ++k) {
        x[k] += v[k] * T;
    }
}

SmartUAV::SmartUAV(double init_x1, double init_x2, double init_x3) : UAV(init_x1, init_x2, init_x3) {}

void SmartUAV::update_and_move(double T, double V, double A, double L, const std::vector<std::unique_ptr<UAV>>& all_uavs, std::mt19937& gen) {
    double min_d = std::numeric_limits<double>::infinity();
    std::vector<std::vector<double>> best_v_choices;
    
    double signs[2] = {1.0, -1.0};
    
    for (int s1 = 0; s1 < 2; ++s1) {
        for (int s2 = 0; s2 < 2; ++s2) {
            for (int s3 = 0; s3 < 2; ++s3) {
                double v_cand[3] = {signs[s1] * V, signs[s2] * V, signs[s3] * V};
                double z[3] = {x[0] + v_cand[0] * T, x[1] + v_cand[1] * T, x[2] + v_cand[2] * T};
                
                double d = 0.0;
                for (const auto& other : all_uavs) {
                    for (int k = 0; k < 3; ++k) {
                        double term = (z[k] - other->get_x(k)) / (2.0 * L);
                        d += term * term;
                    }
                }
                
                if (d < min_d - 1e-9) {
                    min_d = d;
                    best_v_choices.clear();
                    best_v_choices.push_back({v_cand[0], v_cand[1], v_cand[2]});
                } else if (std::abs(d - min_d) <= 1e-9) {
                    best_v_choices.push_back({v_cand[0], v_cand[1], v_cand[2]});
                }
            }
        }
    }
    
    std::uniform_int_distribution<int> dis_choice(0, best_v_choices.size() - 1);
    int choice = dis_choice(gen);
    
    for (int k = 0; k < 3; ++k) {
        x[k] += best_v_choices[choice][k] * T;
    }
}
