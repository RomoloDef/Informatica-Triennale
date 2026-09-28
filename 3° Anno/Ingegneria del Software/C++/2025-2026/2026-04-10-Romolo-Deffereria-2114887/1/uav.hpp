#ifndef UAV_HPP
#define UAV_HPP

#include <random>

class Network;

class UAV {
    double x[3];
    double theta;
    double phi;
    int id;
    Network* net;
public:
    UAV(int id, Network* net, double L, std::mt19937& gen);
    void step(double V, double T, double a, double b, std::mt19937& gen);
    const double* get_position() const { return x; }
    double get_theta() const { return theta; }
    double get_phi() const { return phi; }
};

#endif
