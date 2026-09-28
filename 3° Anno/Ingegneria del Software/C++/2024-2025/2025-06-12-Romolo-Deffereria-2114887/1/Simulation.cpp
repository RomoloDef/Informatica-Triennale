#include "Simulation.hpp"

Simulation::Simulation(double h, int n, double v, double t, std::ofstream& out)
    : H(h), N(n), V(v), T(t), gen(42), outfile(out) {
    
    std::uniform_real_distribution<double> dis_pos(-10.0, 10.0);
    for (int i = 0; i < N; ++i) {
        double init_x = dis_pos(gen);
        double init_y = dis_pos(gen);
        vehicles.push_back(std::make_unique<Vehicle>(init_x, init_y, V));
    }
}

void Simulation::run() {
    double current_time = 0.0;
    while (current_time <= H + 1e-9) {
        for (int i = 0; i < N; ++i) {
            outfile << current_time << " " << (i + 1) << " " 
                    << vehicles[i]->get_x() << " " << vehicles[i]->get_y() << "\n";
        }
        
        if (current_time + T > H + 1e-9) break;

        for (int i = 0; i < N; ++i) {
            vehicles[i]->update_direction(gen);
            vehicles[i]->move(T);
        }
        
        current_time += T;
    }
}
