#ifndef UAV_HPP
#define UAV_HPP

#include <vector>
#include <random>
#include <memory>

class UAV {
protected:
    double x[3];

public:
    UAV(double init_x1, double init_x2, double init_x3);
    virtual ~UAV() = default;

    virtual void update_and_move(double T, double V, double A, double L, const std::vector<std::unique_ptr<UAV>>& all_uavs, std::mt19937& gen);

    double get_x(int k) const { return x[k]; }
};

class SmartUAV : public UAV {
public:
    SmartUAV(double init_x1, double init_x2, double init_x3);
    void update_and_move(double T, double V, double A, double L, const std::vector<std::unique_ptr<UAV>>& all_uavs, std::mt19937& gen) override;
};

#endif // UAV_HPP
