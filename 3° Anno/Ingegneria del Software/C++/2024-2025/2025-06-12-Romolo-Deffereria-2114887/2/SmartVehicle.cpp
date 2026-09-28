#include "SmartVehicle.hpp"
#include <cmath>
#include <algorithm>

SmartVehicle::SmartVehicle(double initial_x, double initial_y, double velocity)
    : Vehicle(initial_x, initial_y, velocity) {}

void SmartVehicle::update_direction(std::mt19937& gen, const std::vector<std::unique_ptr<Vehicle>>& all_vehicles, double R) {
    int quad_counts[4] = {0, 0, 0, 0};
    
    for (const auto& other : all_vehicles) {
        if (other.get() == this) continue;
        
        double ox = other->get_x();
        double oy = other->get_y();
        double dist = std::sqrt(std::pow(ox - x, 2) + std::pow(oy - y, 2));
        
        if (dist <= R) {
            bool dx_pos = (ox - x) >= 0;
            bool dy_pos = (oy - y) >= 0;
            
            if (dx_pos && dy_pos) quad_counts[0]++;
            else if (dx_pos && !dy_pos) quad_counts[1]++;
            else if (!dx_pos && !dy_pos) quad_counts[2]++;
            else if (!dx_pos && dy_pos) quad_counts[3]++;
        }
    }
    
    int min_val = quad_counts[0];
    for (int k = 1; k < 4; ++k) {
        if (quad_counts[k] < min_val) min_val = quad_counts[k];
    }
    
    std::vector<int> min_quads;
    for (int k = 0; k < 4; ++k) {
        if (quad_counts[k] == min_val) {
            min_quads.push_back(k);
        }
    }
    
    std::uniform_int_distribution<int> dis_q(0, min_quads.size() - 1);
    int chosen_quad = min_quads[dis_q(gen)];
    
    std::uniform_real_distribution<double> dis_theta(chosen_quad * M_PI / 2.0, (chosen_quad + 1) * M_PI / 2.0);
    theta = dis_theta(gen);
}
