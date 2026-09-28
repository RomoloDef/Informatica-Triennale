#ifndef SIMULATION_HPP
#define SIMULATION_HPP

#include "Customer.hpp"
#include "Dispatcher.hpp"
#include "Server.hpp"
#include <vector>
#include <memory>

class Simulation {
private:
    double H;
    int N;
    double A;
    double B;
    double T;
    int S;
    int K;
    double p;
    double D;
    double F;
    int seed;

public:
    Simulation(double h, int n, double a, double b, double t, int s, int k, double prob, double d, double f, int random_seed);
    
    // Returns pair<alpha, beta>
    std::pair<long long, long long> run();
};

#endif // SIMULATION_HPP
