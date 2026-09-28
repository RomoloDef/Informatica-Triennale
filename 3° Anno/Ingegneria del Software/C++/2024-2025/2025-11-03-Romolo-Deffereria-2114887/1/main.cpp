#include "MDP.hpp"
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

    string type;
    int N = 0, M = 0;
    
    // First pass: find N to initialize MDP
    while (infile >> type) {
        if (type == "N") {
            infile >> N;
        } else if (type == "M") {
            infile >> M;
        } else if (type == "A") {
            int i, j; double p, c;
            infile >> i >> j >> p >> c;
        }
    }
    
    MDP mdp(N);
    
    // Second pass: load transitions
    infile.clear();
    infile.seekg(0);
    while (infile >> type) {
        if (type == "A") {
            int i, j; double p, c;
            infile >> i >> j >> p >> c;
            mdp.add_transition(i, j, p, c);
        } else if (type == "N" || type == "M") {
            int val; infile >> val;
        }
    }
    infile.close();

    Simulation sim(M, mdp, 42);
    double expected_cost = sim.get_expected_cost();

    ofstream outfile("results.txt");
    if (!outfile) {
        cerr << "Error opening results.txt" << endl;
        return 1;
    }

    outfile << "2025-11-03-Romolo-Deffereria-2114887\n";
    outfile << "C " << expected_cost << "\n";

    outfile.close();
    return 0;
}
