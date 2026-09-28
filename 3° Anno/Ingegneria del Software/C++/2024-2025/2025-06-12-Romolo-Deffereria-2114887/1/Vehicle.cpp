#include "Vehicle.hpp"
#include <cmath>

Vehicle::Vehicle(double initial_x, double initial_y, double velocity)
    : x(initial_x), y(initial_y), v(velocity), theta(0.0) {}

void Vehicle::update_direction(std::mt19937& gen) {
    std::uniform_real_distribution<double> dis_theta(0.0, 2.0 * M_PI);
    theta = dis_theta(gen);
}

void Vehicle::move(double time_step) {
    x += time_step * v * std::sin(theta);
    y += time_step * v * std::cos(theta);
}

double Vehicle::get_x() const {
    return x;
}

double Vehicle::get_y() const {
    return y;
}
