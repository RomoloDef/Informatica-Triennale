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
    double H, V, T;
    int M, N, B, Q;

    infile >> dump >> H;
    infile >> dump >> M;
    infile >> dump >> N;
    infile >> dump >> B;
    infile >> dump >> V;
    infile >> dump >> Q;
    infile >> dump >> T;
    infile.close();

    mt19937 gen_outer(1234);
    uniform_real_distribution<double> dis_A(0.0, 1.0);

    double best_A = 0.0;
    double min_collision_rate = 1e9;

    for (int b_idx = 0; b_idx < B; ++b_idx) {
        double current_A = dis_A(gen_outer);
        long long total_collisions = 0;
        
        for (int m_idx = 0; m_idx < M; ++m_idx) {
            Simulation sim(H, N, current_A, V, Q, T, 42 + b_idx * M + m_idx);
            total_collisions += sim.run_and_get_collisions();
        }
        
        double current_rate = (double)total_collisions / M / H;
        
        if (current_rate < min_collision_rate) {
            min_collision_rate = current_rate;
            best_A = current_A;
        }
    }

    ofstream outfile("results.txt");
    if (!outfile) {
        cerr << "Error opening results.txt" << endl;
        return 1;
    }

    outfile << "2025-07-08-Romolo-Deffereria-2114887\n";
    outfile << "A " << best_A << "\n";
    outfile << "C " << min_collision_rate << "\n";

    outfile.close();
    return 0;
}
