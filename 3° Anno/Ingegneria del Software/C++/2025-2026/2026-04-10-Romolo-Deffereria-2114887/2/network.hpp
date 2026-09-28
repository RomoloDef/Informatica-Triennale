#ifndef NETWORK_HPP
#define NETWORK_HPP

#include <vector>
#include <random>

class UAV;

class Network {
    std::vector<UAV*> uavs;
    int collisions;
public:
    Network();
    ~Network();
    void add_uav(UAV* u);
    void measure_collisions(double D);
    int get_collisions() const { return collisions; }
    void step(double V, double T, double a, double b, double r, std::mt19937& gen);
    const std::vector<UAV*>& get_uavs() const { return uavs; }
};

#endif
