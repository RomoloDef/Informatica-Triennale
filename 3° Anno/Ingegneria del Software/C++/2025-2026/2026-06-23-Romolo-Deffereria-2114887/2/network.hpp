#ifndef NETWORK_HPP
#define NETWORK_HPP

#include "uav.hpp"
#include <vector>

class Network {
private:
    std::vector<UAV*> uavs;
    double D;

public:
    Network(int N, double L, double D, std::mt19937& gen);
    ~Network();

    void step(double V, double T, double a, double b, double r, double A, double B, std::mt19937& gen);

    // Returns the number of collisions at current time
    int count_collisions() const;

    // Returns D(t): the average distance of UAVs to their targets
    double average_target_distance() const;

    const std::vector<UAV*>& get_uavs() const { return uavs; }
};

#endif
