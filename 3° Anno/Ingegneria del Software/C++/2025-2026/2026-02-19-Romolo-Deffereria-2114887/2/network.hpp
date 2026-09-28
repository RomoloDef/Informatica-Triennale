#ifndef NETWORK_HPP
#define NETWORK_HPP

#include "uav.hpp"
#include <vector>

class Network {
private:
  std::vector<UAV> uavs;
  double D;

public:
  Network(int N, double V, double T, double L, int Q, double D);
  void init(std::mt19937 &gen);
  void step(std::mt19937 &gen);
  int countCollisions() const;
};

#endif // NETWORK_HPP.
