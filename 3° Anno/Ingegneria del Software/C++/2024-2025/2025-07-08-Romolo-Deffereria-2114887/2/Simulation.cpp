#include "Simulation.hpp"
#include <cmath>

Simulation::Simulation(double h, int n, double a, double v, int q, double t, int seed)
    : H(h), N(n), A(a), V(v), Q(q), T(t), gen(seed) {
    
    std::uniform_real_distribution<double> dis_pos(-50.0, 50.0);
    
    for (int i = 1; i <= N; ++i) {
        double target_coord = 0.0;
        if (N > 1) {
            target_coord = -50.0 + 100.0 * (i - 1.0) / (N - 1.0);
        }
        
        vehicles.push_back(std::make_unique<Vehicle>(dis_pos(gen), dis_pos(gen), target_coord, target_coord));
    }
}

int Simulation::run_and_get_collisions() {
    double current_time = 0.0;
    int total_collisions = 0;
    
    while (current_time <= H + 1e-9) {
        if (current_time > 0.0) {
            for (auto& v : vehicles) {
                v->choose_and_move(T, V, Q, A, vehicles, gen);
            }
        }
        
        for (int i = 0; i < N; ++i) {
            for (int j = i + 1; j < N; ++j) {
                double dx = vehicles[i]->get_x() - vehicles[j]->get_x();
                double dy = vehicles[i]->get_y() - vehicles[j]->get_y();
                if (std::sqrt(dx*dx + dy*dy) <= 0.1) {
                    total_collisions++;
                }
            }
        }
        
        current_time += T;
    }
    
    return total_collisions;
}
