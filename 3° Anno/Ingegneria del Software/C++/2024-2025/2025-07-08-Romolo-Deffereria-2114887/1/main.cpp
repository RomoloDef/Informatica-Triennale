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
    double H, A, V, T;
    int M, N, Q;

    infile >> dump >> H;
    infile >> dump >> M;
    infile >> dump >> N;
    infile >> dump >> A;
    infile >> dump >> V;
    infile >> dump >> Q;
    infile >> dump >> T;
    infile.close();

    long long total_collisions = 0;
    for (int i = 0; i < M; ++i) {
        Simulation sim(H, N, A, V, Q, T, 42 + i);
        total_collisions += sim.run_and_get_collisions();
    }

    double expected_collision_rate = (double)total_collisions / M / H;

    ofstream outfile("results.txt");
    if (!outfile) {
        cerr << "Error opening results.txt" << endl;
        return 1;
    }

    outfile << "2025-07-08-Romolo-Deffereria-2114887\n";
    outfile << "C " << expected_collision_rate << "\n";

    outfile.close();
    return 0;
}
