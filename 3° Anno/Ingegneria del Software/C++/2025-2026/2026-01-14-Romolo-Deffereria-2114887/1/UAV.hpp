#ifndef UAV_HPP
#define UAV_HPP

class Network;

class UAV {
    double x[3];
    double v[3];
    int id;
    Network* net;
public:
    UAV(int id, Network* net, double L);
    void compute_velocity(double A, double L, double V);
    void move(double T);
    const double* get_position() const { return x; }
};

#endif
