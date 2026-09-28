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
    int M, H, N, S, K;
    double A, B, T, p, D, F;

    infile >> dump >> M;
    infile >> dump >> H;
    infile >> dump >> N;
    infile >> dump >> A;
    infile >> dump >> B;
    infile >> dump >> T;
    infile >> dump >> S;
    infile >> dump >> K;
    infile >> dump >> p;
    infile >> dump >> D;
    infile >> dump >> F;
    infile.close();

    long long total_alpha = 0;
    long long total_beta = 0;

    for (int i = 0; i < M; ++i) {
        Simulation sim(H, N, A, B, T, S, K, p, D, F, 42 + i);
        auto [alpha, beta] = sim.run();
        total_alpha += alpha;
        total_beta += beta;
    }

    double q = 0.0;
    if (total_beta > 0) {
        q = (double)total_alpha / total_beta;
    }

    ofstream outfile("results.txt");
    if (!outfile) {
        cerr << "Error opening results.txt" << endl;
        return 1;
    }

    outfile << "2025-06-12-Romolo-Deffereria-2114887\n";
    outfile << "Q " << q << "\n";

    outfile.close();
    return 0;
}
