#ifndef SIMULATION_HPP
#define SIMULATION_HPP

#include "Customer.hpp"
#include "Provider.hpp"
#include "Server.hpp"
#include <vector>
#include <memory>

class Simulation {
private:
    double T;
    double H;
    int C;
    double A;
    double B;
    int F_prov;
    double V;
    double Q;
    int P;
    int S;
    int K;
    int seed;

public:
    Simulation(double t, double h, int c, double a, double b, int f_prov, double v, double q, int p, int s, int k, int seed);
    
    long long run_and_get_missed_sales();
};

#endif // SIMULATION_HPP
