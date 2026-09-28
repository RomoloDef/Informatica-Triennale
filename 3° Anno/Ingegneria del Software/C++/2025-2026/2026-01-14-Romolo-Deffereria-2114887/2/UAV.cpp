#include "UAV.hpp"
#include "Network.hpp"
#include <cmath>
#include <limits>
#include <random>
#include <vector>

extern std::mt19937 gen;
extern std::uniform_real_distribution<double> dist_unif;

UAV::UAV(int id, Network *net, double L) : id(id), net(net) {
  for (int k = 0; k < 3; ++k) {
    x[k] = -L + 2 * L * dist_unif(gen);
    v[k] = 0;
  }
}

void UAV::compute_velocity(double A, double L, double V, double T) {
  (void)A; // Suppress unused parameter warning
  std::vector<UAV *> uavs = net->get_uavs();
  double min_d = std::numeric_limits<double>::infinity();
  std::vector<std::vector<double> > best_V;

  for (int mask = 0; mask < 8; ++mask) {
    std::vector<double> V_cand(3);
    V_cand[0] = (mask & 1) ? V : -V;
    V_cand[1] = (mask & 2) ? V : -V;
    V_cand[2] = (mask & 4) ? V : -V;

    double z[3];
    z[0] = x[0] + V_cand[0] * T;
    z[1] = x[1] + V_cand[1] * T;
    z[2] = x[2] + V_cand[2] * T;

    double d = 0;
    for (UAV *u : uavs) {
      const double *xj = u->get_position();
      for (int k = 0; k < 3; ++k) {
        double term = (z[k] - xj[k]) / (2.0 * L);
        d += term * term;
      }
    }

    if (d < min_d - 1e-9) {
      min_d = d;
      best_V.clear();
      best_V.push_back(V_cand);
    } else if (std::abs(d - min_d) <= 1e-9) {
      best_V.push_back(V_cand);
    }
  }

  std::uniform_int_distribution<int> dist_idx(0, best_V.size() - 1);
  int idx = dist_idx(gen);
  v[0] = best_V[idx][0];
  v[1] = best_V[idx][1];
  v[2] = best_V[idx][2];
}

void UAV::move(double T) {
  for (int k = 0; k < 3; ++k) {
    x[k] += v[k] * T;
  }
}
