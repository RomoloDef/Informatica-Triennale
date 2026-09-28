#ifndef VEHICLE_HPP
#define VEHICLE_HPP

#include <vector>
#include <random>
#include <memory>

class Vehicle {
protected:
    double x;
    double y;
    double z_x;
    double z_y;

public:
    Vehicle(double initial_x, double initial_y, double target_x, double target_y);
    virtual ~Vehicle() = default;

    virtual void choose_and_move(double T, double V, int Q, double A, const std::vector<std::unique_ptr<Vehicle>>& all_vehicles, std::mt19937& gen);

    double get_x() const { return x; }
    double get_y() const { return y; }
};

#endif // VEHICLE_HPP
