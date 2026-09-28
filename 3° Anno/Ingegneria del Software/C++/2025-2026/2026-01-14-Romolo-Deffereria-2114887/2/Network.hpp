#ifndef NETWORK_HPP
#define NETWORK_HPP

#include <vector>

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
    void step(double A, double L, double V, double T);
    const std::vector<UAV*>& get_uavs() const { return uavs; }
};

#endif
