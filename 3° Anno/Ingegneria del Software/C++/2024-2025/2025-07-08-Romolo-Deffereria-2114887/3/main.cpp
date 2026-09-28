#include "Simulation.hpp"
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    ifstream infile("parameters.txt");
    if (!infile) {
        cerr << "Error opening parameters.txt" << endl;
        return 1;
    }

    string dump;
    int M, N, S, K = 20, Q = 10;
    double H, T, A, B, p, F, G;

    infile >> dump >> H;
    infile >> dump >> T;
    infile >> dump >> M;
    infile >> dump >> N;
    infile >> dump >> A;
    infile >> dump >> B;
    infile >> dump >> p;
    infile >> dump >> S;
    infile >> dump >> F;
    infile >> dump >> G;
    
    if (infile >> dump >> K) {
        if (infile >> dump >> Q) {
            // Read K and Q if present
        }
    }
    infile.close();

    long long total_missed_sales_across_sims = 0;

    for (int i = 0; i < M; ++i) {
        Simulation sim(H, T, N, A, B, p, S, F, G, K, Q, 42 + i);
        auto [missed, w] = sim.run();
        total_missed_sales_across_sims += missed;
    }

    double expected_missed_rate = (double)total_missed_sales_across_sims / M / H;

    ofstream outfile("results.txt");
    if (!outfile) {
        cerr << "Error opening results.txt" << endl;
        return 1;
    }

    outfile << "2025-07-08-Romolo-Deffereria-2114887\n";
    outfile << "V " << expected_missed_rate << "\n";

    outfile.close();
    return 0;
}
