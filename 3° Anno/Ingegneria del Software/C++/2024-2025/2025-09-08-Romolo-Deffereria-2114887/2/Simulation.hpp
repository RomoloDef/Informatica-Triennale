#ifndef SIMULATION_HPP
#define SIMULATION_HPP

#include "UAV.hpp"
#include <vector>
#include <memory>
#include <random>

class Simulation {
private:
    double T;
    double H;
    int N;
    double L;
    double V;
    double A;
    double D;
    std::vector<std::unique_ptr<UAV>> uavs;
    std::mt19937 gen;

public:
    Simulation(double T, double H, int N, double L, double V, double A, double D, int seed);
    int run_and_get_collisions();
};

#endif // SIMULATION_HPP
