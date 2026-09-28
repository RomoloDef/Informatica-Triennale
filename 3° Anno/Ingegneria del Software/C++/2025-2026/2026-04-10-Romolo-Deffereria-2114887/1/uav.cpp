#include "uav.hpp"
#include <cmath>
#include <random>

UAV::UAV(int id, Network* net, double L, std::mt19937& gen) : id(id), net(net) {
    std::uniform_real_distribution<double> dist_pos(-L, L);
    for (int k = 0; k < 3; ++k) {
        x[k] = dist_pos(gen);
    }
    const double PI = std::acos(-1.0);
    std::uniform_real_distribution<double> dist_theta(0.0, PI);
    std::uniform_real_distribution<double> dist_phi(0.0, 2.0 * PI);
    theta = dist_theta(gen);
    phi = dist_phi(gen);
}

void UAV::step(double V, double T, double a, double b, std::mt19937& gen) {
    // Compute velocity from current theta and phi
    double v1 = V * std::sin(theta) * std::cos(phi);
    double v2 = V * std::sin(theta) * std::sin(phi);
    double v3 = V * std::cos(theta);

    // Update position: x_k(t+1) = x_k(t) + T * v_k(t)
    x[0] += T * v1;
    x[1] += T * v2;
    x[2] += T * v3;

    // Update angles: theta(t+1) = theta(t) + T*a*u(t), phi(t+1) = phi(t) + T*b*w(t)
    // u(t) and w(t) chosen uniformly in {-1, 0, 1}
    std::uniform_int_distribution<int> dist_dir(-1, 1);
    int u = dist_dir(gen);
    int w = dist_dir(gen);
    theta += T * a * u;
    phi += T * b * w;
}
