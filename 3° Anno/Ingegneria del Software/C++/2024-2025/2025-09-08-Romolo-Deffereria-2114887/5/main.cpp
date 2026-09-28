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
    double T, H, A, B;
    int M, C, F_prov, G_budget, P, S, K = 20;

    infile >> dump >> T;
    infile >> dump >> H;
    infile >> dump >> M;
    infile >> dump >> C;
    infile >> dump >> A;
    infile >> dump >> B;
    infile >> dump >> F_prov;
    infile >> dump >> G_budget;
    infile >> dump >> P;
    infile >> dump >> S;
    
    if (infile >> dump >> K) {
        // Read K if present
    }
    infile.close();

    mt19937 gen_outer(1234);
    uniform_real_distribution<double> dis_V(0.1, 50.0);

    double best_V = 0.0;
    double best_Q = 0.0;
    double best_R = 0.0;
    double min_J = 1e9;

    for (int g = 0; g < G_budget; ++g) {
        double current_V = dis_V(gen_outer);
        double current_Q = current_V + 5.0;
        
        long long total_missed_sales_across_sims = 0;

        for (int i = 0; i < M; ++i) {
            Simulation sim(T, H, C, A, B, F_prov, current_V, current_Q, P, S, K, 42 + g * M + i);
            total_missed_sales_across_sims += sim.run_and_get_missed_sales();
        }

        double expected_R = (double)total_missed_sales_across_sims / M / H;
        double J = 10.0 * current_V + 2.0 * expected_R;
        
        if (J < min_J) {
            min_J = J;
            best_V = current_V;
            best_Q = current_Q;
            best_R = expected_R;
        }
    }

    ofstream outfile("results.txt");
    if (!outfile) {
        cerr << "Error opening results.txt" << endl;
        return 1;
    }

    outfile << "2025-09-08-Romolo-Deffereria-2114887\n";
    outfile << "R " << best_R << "\n";
    outfile << "V " << best_V << "\n";
    outfile << "Q " << best_Q << "\n";
    outfile << "J " << min_J << "\n";

    outfile.close();
    return 0;
}
