#include "Simulation.hpp"
#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main() {
    ifstream infile("parameters.txt");
    if (!infile) {
        cerr << "Error opening parameters.txt" << endl;
        return 1;
    }

    string dump;
    double H, V, T, R = 2.0;
    int N;

    infile >> dump >> H;
    infile >> dump >> N;
    infile >> dump >> V;
    infile >> dump >> T;
    if (infile >> dump >> R) {
        // read R if available
    }
    infile.close();

    int num_simulations = 1000;
    long long total_collisions = 0;

    for (int i = 0; i < num_simulations; ++i) {
        Simulation sim(H, N, V, T, R, 42 + i);
        total_collisions += sim.run_and_get_collisions();
    }

    double C = 0;
    if (total_collisions > 0) {
        C = (double)(num_simulations * H) / total_collisions;
    } else {
        C = num_simulations * H; // If no collisions ever
    }

    ofstream outfile("results.txt");
    if (!outfile) {
        cerr << "Error opening results.txt" << endl;
        return 1;
    }

    outfile << "2025-06-12-Romolo-Deffereria-2114887\n";
    outfile << "C " << C << "\n";

    outfile.close();
    return 0;
}
