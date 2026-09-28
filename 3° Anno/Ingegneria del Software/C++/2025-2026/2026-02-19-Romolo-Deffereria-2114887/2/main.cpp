#include "network.hpp"
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <random>

int main() {
    std::map<std::string, double> params;
    std::ifstream infile("parameters.txt");
    std::string key;
    double value;
    while (infile >> key >> value) {
        params[key] = value;
    }
    
    double T = params.count("T") ? params["T"] : 1.0;
    double H = params.count("H") ? params["H"] : 10.0;
    int M = params.count("M") ? static_cast<int>(params["M"]) : 100;
    int N = params.count("N") ? static_cast<int>(params["N"]) : 10;
    double L = params.count("L") ? params["L"] : 50.0;
    double V = params.count("V") ? params["V"] : 1.0;
    int Q = params.count("Q") ? static_cast<int>(params["Q"]) : 3;
    double D = params.count("D") ? params["D"] : 1.0; // Default D to 1.0

    double total_collision_rate = 0.0;
    
    std::mt19937 gen(42);

    for (int m = 0; m < M; ++m) {
        Network net(N, V, T, L, Q, D);
        net.init(gen);
        
        int total_collisions = 0;
        
        total_collisions += net.countCollisions();
        
        int steps = static_cast<int>(H / T);
        for (int t = 0; t < steps; ++t) {
            net.step(gen);
            total_collisions += net.countCollisions();
        }
        
        total_collision_rate += static_cast<double>(total_collisions) / H;
    }
    
    double expected_collision_rate = total_collision_rate / M;
    
    std::ofstream outfile("results.txt");
    outfile << "2026-02-19-Romolo-Deffereria-2114887\n";
    outfile << "C " << expected_collision_rate << "\n";
    
    return 0;
}
