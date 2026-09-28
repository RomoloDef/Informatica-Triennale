#ifndef SIMULATION_HPP
#define SIMULATION_HPP

#include "Customer.hpp"
#include "Server.hpp"
#include <vector>
#include <memory>

class Simulation {
private:
    double H;
    double T;
    int N;
    double A;
    double B;
    double p;
    int S;
    double F;
    double G;
    int K;
    int Q;
    int seed;

public:
    Simulation(double h, double t, int n, double a, double b, double p, int s, double f, double g, int k, int q, int seed);
    
    // Returns pair<total_missed_sales, service_rate_w>
    std::pair<long long, double> run();
};

#endif // SIMULATION_HPP
