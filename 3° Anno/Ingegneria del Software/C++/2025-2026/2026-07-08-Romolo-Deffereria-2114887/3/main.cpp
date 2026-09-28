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

    double H = params["H"];
    int M = static_cast<int>(params["M"]);
    int P = static_cast<int>(params["P"]);
    int K = static_cast<int>(params["K"]);
    int C_val = static_cast<int>(params["C"]);
    int V = static_cast<int>(params["V"]);
    double a1 = params["a1"];
    double a2 = params["a2"];
    double a3 = params["a3"];
    double a4 = params["a4"];
    double a5 = params["a5"];
    double a6 = params["a6"];
    double a7 = params["a7"];
    double b1 = params["b1"];
    double b2 = params["b2"];
    double b3 = params["b3"];
    double b4 = params["b4"];
    double b5 = params["b5"];
    double b6 = params["b6"];
    double b7 = params["b7"];
    double r = params["r"];

    double total_R = 0.0;
    std::vector<double> total_Q(C_val, 0.0);

    for (int m = 0; m < M; ++m) {
        std::mt19937 gen(42 + m);
        Network net;
        net.init(P, K, C_val, V, r,
                 a1, b1, a2, b2, a3, b3, a4, b4, a5, b5, a6, b6, a7, b7,
                 gen);

        double R_H;
        std::vector<double> Q;
        net.simulate(H, gen, R_H, Q);

        total_R += R_H;
        for (int i = 0; i < C_val; ++i) {
            total_Q[i] += Q[i];
        }
    }

    double expected_R = total_R / M;
    std::vector<double> expected_Q(C_val);
    for (int i = 0; i < C_val; ++i) {
        expected_Q[i] = total_Q[i] / M;
    }

    
    std::ofstream outfile("results.txt");
    outfile << "2026-07-08-Romolo-Deffereria-2114887" << "\n";
    outfile << "R " << expected_R << "\n";
    for (int i = 0; i < C_val; ++i) {
        outfile << "Q" << (i + 1) << " " << expected_Q[i] << "\n";
    }

    return 0;
}
