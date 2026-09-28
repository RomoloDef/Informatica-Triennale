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
    double T, H, A, B, V, W, p_prob;
    int M, P, K;

    infile >> dump >> T;
    infile >> dump >> H;
    infile >> dump >> M;
    infile >> dump >> A;
    infile >> dump >> B;
    infile >> dump >> V;
    infile >> dump >> W;
    infile >> dump >> P;
    infile >> dump >> K;
    infile >> dump >> p_prob;
    
    infile.close();

    long long total_missed_sales_across_sims = 0;

    for (int i = 0; i < M; ++i) {
        Simulation sim(T, H, A, B, V, W, P, K, p_prob, 42 + i);
        total_missed_sales_across_sims += sim.run_and_get_missed_sales();
    }

    double expected_missed_rate = (double)total_missed_sales_across_sims / M / H;

    ofstream outfile("results.txt");
    if (!outfile) {
        cerr << "Error opening results.txt" << endl;
        return 1;
    }

    outfile << "2025-11-03-Romolo-Deffereria-2114887\n";
    outfile << "R " << expected_missed_rate << "\n";

    outfile.close();
    return 0;
}
