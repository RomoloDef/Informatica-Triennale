#include "uav.hpp"
#include <cmath>
#include <cfloat>

static const double PI = std::acos(-1.0);

UAV::UAV() : x(0), y(0), z(0), active(true) {}

void UAV::init(int index, double L, int K, std::mt19937& gen) {
    std::uniform_real_distribution<double> dist(-K * L, K * L);
    x = dist(gen);
    y = dist(gen);
    z = 10.0 * index;
    active = true;
}

void UAV::stepRandom(double V, double T, std::mt19937& gen) {
    if (!active) return;
    std::uniform_real_distribution<double> dist_theta(0.0, 2.0 * PI);
    double theta = dist_theta(gen);
    x = x + T * V * std::cos(theta);
    y = y + T * V * std::sin(theta);
}

void UAV::stepIntelligent(double V, double T, double P1, int K, double L,
                           const double* /*coverages*/, int /*num_grid*/,
                           std::mt19937& gen) {
    if (!active) return;

    std::uniform_real_distribution<double> dist01(0.0, 1.0);
    double rnd = dist01(gen);

    if (rnd < P1) {
        double best_dist = DBL_MAX;
        int best_h = 0, best_k = 0;
        for (int h = -K; h <= K; ++h) {
            for (int k = -K; k <= K; ++k) {
                double d = distanceTo(h * L, k * L);
                if (d < best_dist) {
                    best_dist = d;
                    best_h = h;
                    best_k = k;
                }
            }
        }

        double target_x = best_h * L;
        double target_y = best_k * L;
        double dx = target_x - x;
        double dy = target_y - y;
        double dist = std::sqrt(dx * dx + dy * dy);

        double theta_star;
        if (dist < 1e-12) {
 
            std::uniform_real_distribution<double> dist_theta(0.0, 2.0 * PI);
            theta_star = dist_theta(gen);
        } else {
            theta_star = std::atan2(dy, dx);
            if (theta_star < 0) theta_star += 2.0 * PI;
        }

        x = x + T * V * std::cos(theta_star);
        y = y + T * V * std::sin(theta_star);
    } else {
        std::uniform_real_distribution<double> dist_theta(0.0, 2.0 * PI);
        double theta = dist_theta(gen);
        x = x + T * V * std::cos(theta);
        y = y + T * V * std::sin(theta);
    }
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
