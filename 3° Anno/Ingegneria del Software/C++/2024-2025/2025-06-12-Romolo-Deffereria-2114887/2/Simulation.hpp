#ifndef SIMULATION_HPP
#define SIMULATION_HPP

#include "Vehicle.hpp"
#include "SmartVehicle.hpp"
#include <vector>
#include <memory>
#include <random>

class Simulation {
private:
    double H;
    int N;
    double V;
    double T;
    double R;
    std::vector<std::unique_ptr<Vehicle>> vehicles;
    std::mt19937 gen;

public:
    Simulation(double H, int N, double V, double T, double R, int seed);
    int run_and_get_collisions();
};

#endif // SIMULATION_HPP
