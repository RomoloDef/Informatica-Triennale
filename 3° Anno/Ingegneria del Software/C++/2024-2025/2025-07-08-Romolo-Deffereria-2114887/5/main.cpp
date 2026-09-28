#include "Simulation.hpp"
#include <iostream>
#include <fstream>
#include <string>
#include <random>

using namespace std;

int main() {
    ifstream infile("parameters.txt");
    if (!infile) {
        cerr << "Error opening parameters.txt" << endl;
        return 1;
    }

    string dump;
    int M, N, S, R_budget, K = 20, Q = 10;
    double H, T, A, B, F, G;

    infile >> dump >> H;
    infile >> dump >> T;
    infile >> dump >> M;
    infile >> dump >> N;
    infile >> dump >> A;
    infile >> dump >> B;
    infile >> dump >> R_budget;
    infile >> dump >> S;
    infile >> dump >> F;
    infile >> dump >> G;
    
    if (infile >> dump >> K) {
        if (infile >> dump >> Q) {
            // Read K and Q if present
        }
    }
    infile.close();

    mt19937 gen_outer(1234);
    uniform_real_distribution<double> dis_p(0.0, 1.0);

    double best_p = 0.0;
    double best_V = 0.0;
    double best_W = -1.0;

    for (int r = 0; r < R_budget; ++r) {
        double current_p = dis_p(gen_outer);
        
        long long total_missed_sales_across_sims = 0;
        double total_w = 0.0;

        for (int i = 0; i < M; ++i) {
            Simulation sim(H, T, N, A, B, current_p, S, F, G, K, Q, 42 + r * M + i);
            auto [missed, w] = sim.run();
            total_missed_sales_across_sims += missed;
            total_w += w;
        }

        double expected_V = (double)total_missed_sales_across_sims / M / H;
        double expected_W = total_w / M;
        
        if (expected_W > best_W) {
            best_W = expected_W;
            best_V = expected_V;
            best_p = current_p;
        }
    }

    ofstream outfile("results.txt");
    if (!outfile) {
        cerr << "Error opening results.txt" << endl;
        return 1;
    }

    outfile << "2025-07-08-Romolo-Deffereria-2114887\n";
    outfile << "P " << best_p << "\n";
    outfile << "V " << best_V << "\n";
    outfile << "W " << best_W << "\n";

    outfile.close();
    return 0;
}
