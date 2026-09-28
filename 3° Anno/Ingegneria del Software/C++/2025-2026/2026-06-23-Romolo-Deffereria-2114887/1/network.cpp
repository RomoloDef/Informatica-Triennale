#include "network.hpp"
#include <cmath>

Network::Network(int N, double L, double D_val, std::mt19937& gen) : D(D_val) {
    for (int i = 0; i < N; ++i) {
        uavs.push_back(new UAV(L, gen));
    }
}

Network::~Network() {
    for (auto u : uavs) {
        delete u;
    }
}

void Network::step(double V, double T, double a, double b, std::mt19937& gen) {
    for (auto u : uavs) {
        u->step(V, T, a, b, gen);
    }
}

int Network::count_collisions() const {
    int collisions = 0;
    int N = uavs.size();
    for (int i = 0; i < N; ++i) {
        const double* p1 = uavs[i]->get_position();
        for (int j = i + 1; j < N; ++j) {
            const double* p2 = uavs[j]->get_position();
            double dist_sq = 0.0;
            for (int k = 0; k < 3; ++k) {
                double diff = p1[k] - p2[k];
                dist_sq += diff * diff;
            }
            if (std::sqrt(dist_sq) < D) {
                collisions++;
            }
        }
    }
    return collisions;
}

double Network::average_target_distance() const {
    double total_dist = 0.0;
    for (auto u : uavs) {
        total_dist += u->distance_to_target();
    }
    if (uavs.empty()) return 0.0;
    return total_dist / uavs.size();
}
