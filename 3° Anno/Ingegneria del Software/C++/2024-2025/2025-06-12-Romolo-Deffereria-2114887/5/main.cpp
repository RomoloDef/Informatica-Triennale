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
    int M, W_budget, H, N, S, K;
    double A, B, T, D, F;

    infile >> dump >> M;
    infile >> dump >> W_budget;
    infile >> dump >> H;
    infile >> dump >> N;
    infile >> dump >> A;
    infile >> dump >> B;
    infile >> dump >> T;
    infile >> dump >> S;
    infile >> dump >> K;
    infile >> dump >> D;
    infile >> dump >> F;
    infile.close();

    mt19937 gen(12345);
    uniform_real_distribution<double> dis_p(0.0, 1.0);

    double best_p = 0.0;
    double best_q = 1e9; // minimize q

    for (int w = 0; w < W_budget; ++w) {
        double current_p = dis_p(gen);
        
        long long total_alpha = 0;
        long long total_beta = 0;

        for (int i = 0; i < M; ++i) {
            // Seed uniquely for each simulation but deterministically
            Simulation sim(H, N, A, B, T, S, K, current_p, D, F, 42 + w * M + i);
            auto [alpha, beta] = sim.run();
            total_alpha += alpha;
            total_beta += beta;
        }

        double q = 0.0;
        if (total_beta > 0) {
            q = (double)total_alpha / total_beta;
        }
        
        if (q < best_q) {
            best_q = q;
            best_p = current_p;
        }
    }

    ofstream outfile("results.txt");
    if (!outfile) {
        cerr << "Error opening results.txt" << endl;
        return 1;
    }

    outfile << "2025-06-12-Romolo-Deffereria-2114887\n";
    outfile << "P " << best_p << "\n";
    outfile << "Q " << best_q << "\n";

    outfile.close();
    return 0;
}
