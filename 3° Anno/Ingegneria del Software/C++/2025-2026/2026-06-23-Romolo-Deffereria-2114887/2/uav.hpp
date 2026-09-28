#ifndef UAV_HPP
#define UAV_HPP

#include <random>

class Network;

class UAV {
private:
    int id;
    Network* net;
    double x[3];
    double z[3]; // target
    double theta;
    double phi;

public:
    UAV(int id, Network* net, double L, std::mt19937& gen);

    // Compute step: chooses u,w to minimize J(i, t+2)
    void step(double V, double T, double a, double b, double r, double A, double B, std::mt19937& gen);

    const double* get_position() const { return x; }
    const double* get_target() const { return z; }
    
    // Distance from current position to target
    double distance_to_target() const;
};

#endif
