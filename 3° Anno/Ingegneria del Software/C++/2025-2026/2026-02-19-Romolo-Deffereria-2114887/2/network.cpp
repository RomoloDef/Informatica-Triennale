#include "network.hpp"
#include <cmath>

Network::Network(int N, double V, double T, double L, int Q, double D) : D(D) {
    uavs.reserve(N);
    for (int i = 0; i < N; ++i) {
        uavs.emplace_back(i + 1, V, T, L, Q);
    }
}

void Network::init(std::mt19937& gen) {
    for (auto& uav : uavs) {
        uav.init(gen);
    }
}

void Network::step(std::mt19937& gen) {
    // Gather all current positions
    std::vector<std::vector<double> > all_positions;
    all_positions.reserve(uavs.size());
    for (const auto& uav : uavs) {
        all_positions.push_back(uav.getPosition());
    }

    // Update each UAV
    for (auto& uav : uavs) {
        uav.update(gen, all_positions);
    }
}

int Network::countCollisions() const {
    int collisions = 0;
    int N = uavs.size();
    for (int i = 0; i < N; ++i) {
        auto pos1 = uavs[i].getPosition();
        bool collision_found = false;
        for (int j = i + 1; j < N; ++j) {
            auto pos2 = uavs[j].getPosition();
            double dist_sq = 0;
            for (int k = 0; k < 3; ++k) {
                double diff = pos1[k] - pos2[k];
                dist_sq += diff * diff;
            }
            if (std::sqrt(dist_sq) < D) {
                collision_found = true;
                break;
            }
        }
        if (collision_found) {
            collisions++;
        }
    }
    return collisions;
}
