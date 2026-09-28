#include "network.hpp"
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <cmath>
#include <algorithm>
#include <numeric>

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

    double base = 0.5;
    double a_coeff = (1.0 - base) / (1.0 - std::pow(base, K));
    std::vector<double> p_vals(K);
    for (int j = 0; j < K; ++j) {
        p_vals[j] = a_coeff * std::pow(base, j);
    }

    std::vector<int> perm_indices(K);
    std::iota(perm_indices.begin(), perm_indices.end(), 0);


    std::vector<std::vector<std::vector<double>>> best_probs(
        C_val, std::vector<std::vector<double>>(P, std::vector<double>(K, 1.0 / K)));

    for (int ci = 0; ci < C_val; ++ci) {
        for (int pj = 0; pj < P; ++pj) {
            bool uses_product = false;
            for (int v = 0; v < V; ++v) {
                if (best_probs[ci][pj][0] >= 0) { 
                }
            }
            std::vector<int> perm(K);
            std::iota(perm.begin(), perm.end(), 0);
            
            double best_Q = 1e18;
            std::vector<double> best_assignment(K, 1.0 / K);
            
            do {
                std::vector<std::vector<std::vector<double>>> test_probs = best_probs;
                for (int l = 0; l < K; ++l) {
                    test_probs[ci][pj][l] = p_vals[perm[l]];
                }
                
                double total_Q_ci = 0.0;
                for (int m = 0; m < M; ++m) {
                    std::mt19937 gen(42 + m);
                    Network net;
                    net.init(P, K, C_val, V, r,
                             a1, b1, a2, b2, a3, b3, a4, b4, a5, b5, a6, b6, a7, b7,
                             gen);
                    double R_H;
                    std::vector<double> Q;
                    net.simulate(H, gen, R_H, Q, test_probs);
                    total_Q_ci += Q[ci];
                }
                
                double avg_Q_ci = total_Q_ci / M;
                if (avg_Q_ci < best_Q) {
                    best_Q = avg_Q_ci;
                    best_assignment.assign(K, 0);
                    for (int l = 0; l < K; ++l) {
                        best_assignment[l] = p_vals[perm[l]];
                    }
                }
            } while (std::next_permutation(perm.begin(), perm.end()));
            
            best_probs[ci][pj] = best_assignment;
        }
    }

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
        net.simulate(H, gen, R_H, Q, best_probs);
        total_R += R_H;
        for (int i = 0; i < C_val; ++i) {
            total_Q[i] += Q[i];
        }
    }

    double expected_R = total_R / M;

    std::ofstream outfile("results.txt");
    outfile << "2026-07-08-Romolo-Deffereria-2114887" << "\n";
    outfile << "R " << expected_R << "\n";
    for (int i = 0; i < C_val; ++i) {
        outfile << "Q" << (i + 1) << " " << total_Q[i] / M << "\n";
    }

    return 0;
}
