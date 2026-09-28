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
    int Q;

public:
    UAV(int id, double V, double T, double L, int Q);
    void init(std::mt19937& gen);
    void update(std::mt19937& gen, const std::vector<std::vector<double> >& all_positions);
    std::vector<double> getPosition() const;
    void setPosition(const std::vector<double>& new_pos);
};

#endif // UAV_HPP
