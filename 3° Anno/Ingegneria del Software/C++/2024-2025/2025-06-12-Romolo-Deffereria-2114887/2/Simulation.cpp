#include "Simulation.hpp"
#include <cmath>

Simulation::Simulation(double h, int n, double v, double t, double r, int seed)
    : H(h), N(n), V(v), T(t), R(r), gen(seed) {
    
    std::uniform_real_distribution<double> dis_pos(-10.0, 10.0);
    for (int i = 0; i < N; ++i) {
        double init_x = dis_pos(gen);
        double init_y = dis_pos(gen);
        if (i == 0) {
            vehicles.push_back(std::make_unique<SmartVehicle>(init_x, init_y, V));
        } else {
            vehicles.push_back(std::make_unique<Vehicle>(init_x, init_y, V));
        }
    }
}

int Simulation::run_and_get_collisions() {
    double current_time = 0.0;
    int collision_count = 0;
    
    while (current_time <= H + 1e-9) {
        if (current_time + T > H + 1e-9) break;

        for (int i = 0; i < N; ++i) {
            vehicles[i]->update_direction(gen, vehicles, R);
        }
        
        for (int i = 0; i < N; ++i) {
            vehicles[i]->move(T);
        }
        
        // Count collisions for vehicle 1 (index 0)
        double x1 = vehicles[0]->get_x();
        double y1 = vehicles[0]->get_y();
        for (int j = 1; j < N; ++j) {
            double ox = vehicles[j]->get_x();
            double oy = vehicles[j]->get_y();
            double dist = std::sqrt(std::pow(ox - x1, 2) + std::pow(oy - y1, 2));
            if (dist <= R) {
                collision_count++;
            }
        }
        
        current_time += T;
    }
    
    return collision_count;
}
