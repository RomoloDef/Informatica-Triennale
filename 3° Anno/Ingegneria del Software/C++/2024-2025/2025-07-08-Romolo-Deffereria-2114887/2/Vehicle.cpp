#include "Vehicle.hpp"
#include <cmath>
#include <limits>

Vehicle::Vehicle(double initial_x, double initial_y, double target_x, double target_y)
    : x(initial_x), y(initial_y), z_x(target_x), z_y(target_y) {}

void Vehicle::choose_and_move(double T, double V, int Q, double A, const std::vector<std::unique_ptr<Vehicle>>& all_vehicles, std::mt19937& gen) {
    double best_theta = 0.0;
    double min_F = std::numeric_limits<double>::infinity();

    for (int k = 0; k < Q; ++k) {
        double theta = (double)k / Q * 2.0 * M_PI;
        
        double cand_x = x + T * V * std::sin(theta);
        double cand_y = y + T * V * std::cos(theta);
        
        double term1 = std::pow(cand_x - z_x, 2) + std::pow(cand_y - z_y, 2);
        
        double term2 = 0.0;
        for (const auto& other : all_vehicles) {
            if (other.get() != this) {
                term2 += std::pow(other->get_x() - cand_x, 2) + std::pow(other->get_y() - cand_y, 2);
            }
        }
        
        double F = A * term1 - (1.0 - A) * term2;
        
        if (F < min_F) {
            min_F = F;
            best_theta = theta;
        }
    }
    
    std::uniform_real_distribution<double> dis_w(-2.0 * M_PI / Q, 2.0 * M_PI / Q);
    double w1 = dis_w(gen);
    double w2 = dis_w(gen);
    
    x += T * V * std::sin(best_theta + w1);
    y += T * V * std::cos(best_theta + w2);
}
