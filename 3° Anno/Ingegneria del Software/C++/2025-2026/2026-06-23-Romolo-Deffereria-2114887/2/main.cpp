#include "network.hpp"
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <cmath>

int main() {
    std::map<std::string, double> params;
    std::ifstream infile("parameters.txt");
    std::string key;
    double value;
    while (infile >> key >> value) {
        params[key] = value;
    }

    double T = params["T"];
    double H = params["H"];
    int M = static_cast<int>(params["M"]);
    int N = static_cast<int>(params["N"]);
    double L = params["L"];
    double V = params["V"];
    double a = params["a"];
    double b = params["b"];
    double r = params["r"];
    double A = params["A"];
    double B_val = params["B"]; // renamed to avoid conflict
    
    // Use D if provided, otherwise default to 1.0
    double D = params.count("D") ? params["D"] : 1.0;

    int steps = static_cast<int>(std::round(H / T));
    
    double total_collisions = 0.0;
    double total_final_dist = 0.0;

    for (int m = 0; m < M; ++m) {
        std::mt19937 gen(42 + m);
        Network net(N, L, D, gen);

        int coll = 0;
        // Collision at t=0
        coll += net.count_collisions();

        for (int s = 0; s < steps; ++s) {
            net.step(V, T, a, b, r, A, B_val, gen);
            coll += net.count_collisions();
        }

        total_collisions += coll;
        total_final_dist += net.average_target_distance();
    }

    double C = total_collisions / (M * H);
    double D_final = total_final_dist / M;

    std::ofstream outfile("results.txt");
    outfile << "2026-06-23-Romolo-Deffereria-2114887\n";
    outfile << "C " << C << " D " << D_final << "\n";

    return 0;
}
