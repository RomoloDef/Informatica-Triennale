#include "uav.hpp"
#include "network.hpp"
#include <cmath>
#include <limits>
#include <random>
#include <utility>
#include <vector>

UAV::UAV(int id, Network *net, double L, std::mt19937 &gen) : id(id), net(net) {
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

void UAV::step(double V, double T, double a, double b, double r,
               std::mt19937 &gen) {
  // Step 1: Find neighbors within distance r
  const auto &uavs = net->get_uavs();
  std::vector<int> neighbors;
  for (int j = 0; j < (int)uavs.size(); ++j) {
    if (uavs[j] == this)
      continue;
    const double *xj = uavs[j]->get_position();
    double dist_sq = 0;
    for (int k = 0; k < 3; ++k) {
      double diff = x[k] - xj[k];
      dist_sq += diff * diff;
    }
    if (std::sqrt(dist_sq) <= r) {
      neighbors.push_back(j);
    }
  }

  if (neighbors.empty()) {
    // No neighbors: choose u, w randomly as in exercise 1
    double v1 = V * std::sin(theta) * std::cos(phi);
    double v2 = V * std::sin(theta) * std::sin(phi);
    double v3 = V * std::cos(theta);
    x[0] += T * v1;
    x[1] += T * v2;
    x[2] += T * v3;

    std::uniform_int_distribution<int> dist_dir(-1, 1);
    int u = dist_dir(gen);
    int w = dist_dir(gen);
    theta += T * a * u;
    phi += T * b * w;
    return;
  }

  // Step 2: Try all 9 combinations of (u, w) in {-1, 0, 1}
  // Compute position at t+2 for each and find the one maximizing F(t+2, i)
  // F(t+2,i) = min distance to neighbors (assuming neighbors don't move)
  double best_F = -1.0;
  std::vector<std::pair<int, int>> best_choices;

  for (int u_val = -1; u_val <= 1; ++u_val) {
    for (int w_val = -1; w_val <= 1; ++w_val) {
      // Compute theta(t+1) and phi(t+1)
      double theta1 = theta + T * a * u_val;
      double phi1 = phi + T * b * w_val;

      // Compute v(t) from current theta, phi
      double v1_t = V * std::sin(theta) * std::cos(phi);
      double v2_t = V * std::sin(theta) * std::sin(phi);
      double v3_t = V * std::cos(theta);

      // Compute x(t+1) = x(t) + T*v(t)
      double x1[3];
      x1[0] = x[0] + T * v1_t;
      x1[1] = x[1] + T * v2_t;
      x1[2] = x[2] + T * v3_t;

      // Compute v(t+1) from theta1, phi1
      double v1_t1 = V * std::sin(theta1) * std::cos(phi1);
      double v2_t1 = V * std::sin(theta1) * std::sin(phi1);
      double v3_t1 = V * std::cos(theta1);

      // Compute x(t+2) = x(t+1) + T*v(t+1)
      double x2[3];
      x2[0] = x1[0] + T * v1_t1;
      x2[1] = x1[1] + T * v2_t1;
      x2[2] = x1[2] + T * v3_t1;

      // Compute F(t+2, i) = min distance to neighbors (at their current
      // positions)
      double min_dist = std::numeric_limits<double>::max();
      for (int idx : neighbors) {
        const double *xn = uavs[idx]->get_position();
        double dist_sq = 0;
        for (int k = 0; k < 3; ++k) {
          double diff = x2[k] - xn[k];
          dist_sq += diff * diff;
        }
        double d = std::sqrt(dist_sq);
        if (d < min_dist)
          min_dist = d;
      }

      if (best_choices.empty() || min_dist > best_F + 1e-9) {
        best_F = min_dist;
        best_choices.clear();
        best_choices.push_back({u_val, w_val});
      } else if (std::abs(min_dist - best_F) <= 1e-9) {
        best_choices.push_back({u_val, w_val});
      }
    }
  }

  // Choose one optimal (u, w) uniformly at random
  int chosen_u, chosen_w;
  if (best_choices.size() == 1) {
    chosen_u = best_choices[0].first;
    chosen_w = best_choices[0].second;
  } else {
    std::uniform_int_distribution<int> dist(0, best_choices.size() - 1);
    int idx = dist(gen);
    chosen_u = best_choices[idx].first;
    chosen_w = best_choices[idx].second;
  }

  // Apply the chosen (u, w): update position and angles
  double v1 = V * std::sin(theta) * std::cos(phi);
  double v2 = V * std::sin(theta) * std::sin(phi);
  double v3 = V * std::cos(theta);
  x[0] += T * v1;
  x[1] += T * v2;
  x[2] += T * v3;

  theta += T * a * chosen_u;
  phi += T * b * chosen_w;
}
