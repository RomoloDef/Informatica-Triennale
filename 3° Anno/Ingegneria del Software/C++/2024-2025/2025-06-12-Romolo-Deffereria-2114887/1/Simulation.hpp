#ifndef SIMULATION_HPP
#define SIMULATION_HPP

#include "Vehicle.hpp"
#include <vector>
#include <memory>
#include <string>
#include <fstream>

class Simulation {
private:
    double H;
    int N;
    double V;
    double T;
    std::vector<std::unique_ptr<Vehicle>> vehicles;
    std::mt19937 gen;
    std::ofstream& outfile;

public:
    Simulation(double H, int N, double V, double T, std::ofstream& out);
    void run();
};

#endif // SIMULATION_HPP
