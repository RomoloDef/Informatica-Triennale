#ifndef SIMULATION_HPP
#define SIMULATION_HPP

#include "Vehicle.hpp"
#include <vector>
#include <memory>
#include <random>

class Simulation {
private:
    double H;
    int N;
    double A;
    double V;
    int Q;
    double T;
    std::vector<std::unique_ptr<Vehicle>> vehicles;
    std::mt19937 gen;

public:
    Simulation(double H, int N, double A, double V, int Q, double T, int seed);
    int run_and_get_collisions();
};

#endif // SIMULATION_HPP
