#ifndef UAV_HPP
#define UAV_HPP

#include <random>
#include <vector>

class UAV {
private:
    double x[3] = {0.0, 0.0, 0.0};
    double V;
    double T;
    double L;

public:
    UAV(int id, double V, double T, double L);
    void init(std::mt19937& gen);
    void update(std::mt19937& gen);
    std::vector<double> getPosition() const;
};

#endif // UAV_HPP
