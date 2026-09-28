#include "Simulation.hpp"
#include <cmath>

Simulation::Simulation(double t_step, double h, int n, double l, double v, double a, double d, int seed)
    : T(t_step), H(h), N(n), L(l), V(v), A(a), D(d), gen(seed) {
    
    std::uniform_real_distribution<double> dis_pos(-L, L);
    
    for (int i = 0; i < N; ++i) {
        // Ex 2 uses SmartUAV instead of regular UAV
        uavs.push_back(std::make_unique<SmartUAV>(dis_pos(gen), dis_pos(gen), dis_pos(gen)));
    }
}

int Simulation::run_and_get_collisions() {
    double current_time = 0.0;
    int total_collisions = 0;
    
    while (current_time <= H + 1e-9) {
        if (current_time > 0.0) {
            for (auto& u : uavs) {
                u->update_and_move(T, V, A, L, uavs, gen);
            }
        }
        
        for (int i = 0; i < N; ++i) {
            for (int j = i + 1; j < N; ++j) {
                double dist_sq = 0.0;
                for (int k = 0; k < 3; ++k) {
                    double diff = uavs[i]->get_x(k) - uavs[j]->get_x(k);
                    dist_sq += diff * diff;
                }
                if (std::sqrt(dist_sq) <= D) {
                    total_collisions++;
                }
            }
        }
        
        current_time += T;
    }
    
    return total_collisions;
}
