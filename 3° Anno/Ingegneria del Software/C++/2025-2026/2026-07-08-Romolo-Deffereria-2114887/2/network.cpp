#include "network.hpp"
#include <cmath>

Network::Network() : N(0), K(0), L(0) {}

void Network::init(int n, int k, double l, std::mt19937& gen) {
    N = n;
    K = k;
    L = l;
    uavs.resize(N);
    for (int i = 0; i < N; ++i) {
        uavs[i].init(i + 1, L, K, gen);
    }
}

void Network::reset(int n, int k, double l, std::mt19937& gen) {
    N = n;
    K = k;
    L = l;
    uavs.resize(N);
    for (int i = 0; i < N; ++i) {
        uavs[i].init(i + 1, L, K, gen);
    }
}

void Network::step(double V, double T, double PFAIL, double PREC, std::mt19937& gen) {
    for (int i = 0; i < N; ++i) {
        uavs[i].updateStatus(PFAIL, PREC, gen);
        uavs[i].stepRandom(V, T, gen);
    }
}

void Network::stepIntelligent(double V, double T, double PFAIL, double PREC, double P1, std::mt19937& gen) {
    for (int i = 0; i < N; ++i) {
        uavs[i].updateStatus(PFAIL, PREC, gen);
        uavs[i].stepIntelligent(V, T, P1, K, L, nullptr, 0, gen);
    }
}

int Network::coverage(double r, int h, int k) const {
    int count = 0;
    double hL = h * L;
    double kL = k * L;
    for (int i = 0; i < N; ++i) {
        if (uavs[i].isActive() && uavs[i].distanceTo(hL, kL) <= r) {
            count++;
        }
    }
    return count;
}

double Network::avgCoverage(double r) const {
    double total = 0.0;
    int gridSize = 2 * K + 1;
    int totalPoints = gridSize * gridSize;
    for (int h = -K; h <= K; ++h) {
        for (int k = -K; k <= K; ++k) {
            total += coverage(r, h, k);
        }
    }
    return total / totalPoints;
}

double Network::stdDevCoverage(double r) const {
    double mean = avgCoverage(r);
    double totalSqDiff = 0.0;
    int gridSize = 2 * K + 1;
    int totalPoints = gridSize * gridSize;
    for (int h = -K; h <= K; ++h) {
        for (int k = -K; k <= K; ++k) {
            double diff = coverage(r, h, k) - mean;
            totalSqDiff += diff * diff;
        }
    }
    return std::sqrt(totalSqDiff / totalPoints);
}
