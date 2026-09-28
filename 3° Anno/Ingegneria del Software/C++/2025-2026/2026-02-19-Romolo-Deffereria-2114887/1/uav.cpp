#include "uav.hpp"
#include <cmath>

UAV::UAV(int id, double V, double T, double L) 
    : V(V), T(T), L(L) {
    (void)id; // to avoid unused parameter warning
}

void UAV::init(std::mt19937& gen) {
    std::uniform_real_distribution<double> dist_pos(-L, L);
    x[0] = dist_pos(gen);
    x[1] = dist_pos(gen);
    x[2] = dist_pos(gen);
}

void UAV::update(std::mt19937& gen) {
    const double PI = std::acos(-1.0);
    std::uniform_real_distribution<double> dist_theta(0.0, PI);
    std::uniform_real_distribution<double> dist_phi(0.0, 2.0 * PI);
    
    double theta = dist_theta(gen);
    double phi = dist_phi(gen);
    
    double v1 = V * std::sin(theta) * std::cos(phi);
    double v2 = V * std::sin(theta) * std::sin(phi);
    double v3 = V * std::cos(theta);
    
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
