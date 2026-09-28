#ifndef VEHICLE_HPP
#define VEHICLE_HPP

#include <random>
#include <vector>
#include <memory>

class Vehicle {
protected:
    double x;
    double y;
    double v;
    double theta;

public:
    Vehicle(double initial_x, double initial_y, double velocity);
    virtual ~Vehicle() = default;

    virtual void update_direction(std::mt19937& gen, const std::vector<std::unique_ptr<Vehicle>>& all_vehicles, double R);
    virtual void move(double time_step);

    double get_x() const;
    double get_y() const;
};

#endif // VEHICLE_HPP
