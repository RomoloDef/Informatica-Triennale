#ifndef SMART_VEHICLE_HPP
#define SMART_VEHICLE_HPP

#include "Vehicle.hpp"

class SmartVehicle : public Vehicle {
public:
    SmartVehicle(double initial_x, double initial_y, double velocity);
    
    void update_direction(std::mt19937& gen, const std::vector<std::unique_ptr<Vehicle>>& all_vehicles, double R) override;
};

#endif // SMART_VEHICLE_HPP
