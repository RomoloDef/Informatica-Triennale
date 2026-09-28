#include "uav.hpp"
#include <cmath>

UAV::UAV() : x(0), y(0), z(0), active(true) {}

void UAV::init(int index, double L, int K, std::mt19937& gen) {
    std::uniform_real_distribution<double> dist(-K * L, K * L);
    x = dist(gen);
    y = dist(gen);
    z = 10.0 * index;
    active = true;
}

void UAV::step(double V, double T, std::mt19937& gen) {
    if (!active) return;
    const double PI = std::acos(-1.0);
    std::uniform_real_distribution<double> dist_theta(0.0, 2.0 * PI);
    double theta = dist_theta(gen);
    x = x + T * V * std::cos(theta);
    y = y + T * V * std::sin(theta);
}

void UAV::updateStatus(double PFAIL, double PREC, std::mt19937& gen) {
    std::uniform_real_distribution<double> dist(0.0, 1.0);
    double r = dist(gen);
    if (active) {
        if (r < PFAIL) {
            active = false;
        }
    } else {
        if (r < PREC) {
            active = true;
        }
    }
}

double UAV::distanceTo(double hL, double kL) const {
    return std::sqrt((x - hL) * (x - hL) + (y - kL) * (y - kL));
}
