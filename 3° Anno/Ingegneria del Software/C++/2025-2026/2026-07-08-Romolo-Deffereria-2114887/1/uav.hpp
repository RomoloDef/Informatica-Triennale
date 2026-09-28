#ifndef UAV_HPP
#define UAV_HPP

#include <random>

class UAV {
private:
    double x, y, z;
    bool active;

public:
    UAV();
    void init(int index, double L, int K, std::mt19937& gen);
    void step(double V, double T, std::mt19937& gen);
    void updateStatus(double PFAIL, double PREC, std::mt19937& gen);

    double getX() const { return x; }
    double getY() const { return y; }
    double getZ() const { return z; }
    bool isActive() const { return active; }

    double distanceTo(double hL, double kL) const;
};

#endif
