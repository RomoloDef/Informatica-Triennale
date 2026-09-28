#include "UAV.hpp"
#include <cmath>
#include <random>

extern std::mt19937 gen;
extern std::uniform_real_distribution<double> dist_unif;

UAV::UAV(int id, Network* net, double L) : id(id), net(net) {
    for (int k = 0; k < 3; ++k) {
        x[k] = -L + 2 * L * dist_unif(gen);
        v[k] = 0;
    }
}

void UAV::compute_velocity(double A, double L, double V) {
    for (int k = 0; k < 3; ++k) {
        double p = std::exp(-A * (x[k] + L) / (2.0 * L));
        double r = dist_unif(gen);
        if (r <= p) {
            v[k] = V;
        } else {
            v[k] = -V;
        }
    }
}

void UAV::move(double T) {
    for (int k = 0; k < 3; ++k) {
        x[k] += v[k] * T;
    }
}
