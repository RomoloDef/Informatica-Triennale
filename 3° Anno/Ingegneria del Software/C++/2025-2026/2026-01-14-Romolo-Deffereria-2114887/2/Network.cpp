#include "Network.hpp"
#include "UAV.hpp"
#include <cmath>

Network::Network() : collisions(0) {}

Network::~Network() {
    for (auto u : uavs) delete u;
}

void Network::add_uav(UAV* u) {
    uavs.push_back(u);
}

void Network::step(double A, double L, double V, double T) {
    for (auto u : uavs) {
        u->compute_velocity(A, L, V, T);
    }
    for (auto u : uavs) {
        u->move(T);
    }
}

void Network::measure_collisions(double D) {
    int n = uavs.size();
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            const double* x_i = uavs[i]->get_position();
            const double* x_j = uavs[j]->get_position();
            double dist_sq = 0;
            for (int k = 0; k < 3; ++k) {
                double diff = x_i[k] - x_j[k];
                dist_sq += diff * diff;
            }
            if (std::sqrt(dist_sq) <= D) {
                collisions++;
            }
        }
    }
}
