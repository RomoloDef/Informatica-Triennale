#ifndef SIMULATION_HPP
#define SIMULATION_HPP

#include "Customer.hpp"
#include "Server.hpp"
#include <memory>

class Simulation {
private:
    double T;
    double H;
    double A;
    double B;
    double V;
    double W;
    int P;
    int K;
    double p;
    int seed;

public:
    Simulation(double t, double h, double a, double b, double v, double w, int p_val, int k_val, double prob, int seed);
    
    long long run_and_get_missed_sales();
};

#endif // SIMULATION_HPP
