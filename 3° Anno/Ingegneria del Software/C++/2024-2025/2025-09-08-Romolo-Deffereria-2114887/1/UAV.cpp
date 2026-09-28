#include "UAV.hpp"
#include <cmath>
#include <algorithm>

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
