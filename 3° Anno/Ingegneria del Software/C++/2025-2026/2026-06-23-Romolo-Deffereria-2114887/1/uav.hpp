#ifndef UAV_HPP
#define UAV_HPP

#include <random>

class Network;

class UAV {
private:
    double x[3];
    double z[3]; // target
    double theta;
    double phi;

public:
    UAV(double L, std::mt19937& gen);

    // Compute step: chooses u,w to minimize distance to target at t+2,
    // then updates position x to t+1 and angles to t+1.
    void step(double V, double T, double a, double b, std::mt19937& gen);

    const double* get_position() const { return x; }
    const double* get_target() const { return z; }
    
    // Distance from current position to target
    double distance_to_target() const;
};

#endif
