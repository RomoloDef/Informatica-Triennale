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
    double T, H, A, B_param, V, W, G_cost;
    int M, P, K, B_opt;

    infile >> dump >> T;
    infile >> dump >> H;
    infile >> dump >> M;
    infile >> dump >> A;
    infile >> dump >> B_param;
    infile >> dump >> V;
    infile >> dump >> W;
    infile >> dump >> P;
    infile >> dump >> K;
    infile >> dump >> B_opt;
    infile >> dump >> G_cost;
    
    infile.close();

    mt19937 gen_outer(1234);
    uniform_real_distribution<double> dis_p(0.0, 1.0);

    double best_p = 0.0;
    double best_R = 0.0;
    double min_J = 1e9;

    for (int b = 0; b < B_opt; ++b) {
        double current_p = dis_p(gen_outer);
        
        long long total_missed_sales_across_sims = 0;

        for (int i = 0; i < M; ++i) {
            Simulation sim(T, H, A, B_param, V, W, P, K, current_p, 42 + b * M + i);
            total_missed_sales_across_sims += sim.run_and_get_missed_sales();
        }

        double expected_R = (double)total_missed_sales_across_sims / M / H;
        double J = G_cost * current_p + expected_R;
        
        if (J < min_J) {
            min_J = J;
            best_p = current_p;
            best_R = expected_R;
        }
    }

    ofstream outfile("results.txt");
    if (!outfile) {
        cerr << "Error opening results.txt" << endl;
        return 1;
    }

    outfile << "2025-11-03-Romolo-Deffereria-2114887\n";
    outfile << "p " << best_p << "\n";
    outfile << "R " << best_R << "\n";
    outfile << "J " << min_J << "\n";

    outfile.close();
    return 0;
}
