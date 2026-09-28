#include "ParameterizedMDP.hpp"
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

    string type;
    int N = 0, M = 0, B = 0;
    double K_cost = 0.0;
    double c00 = 0.0, c01 = 0.0;
    
    while (infile >> type) {
        if (type == "N") infile >> N;
        else if (type == "M") infile >> M;
        else if (type == "B") infile >> B;
        else if (type == "K") infile >> K_cost;
        else if (type == "A") {
            int i, j; double p, c;
            infile >> i >> j >> p >> c;
            if (i == 0 && j == 0) c00 = c;
            else if (i == 0 && j == 1) c01 = c;
        }
    }
    
    ParameterizedMDP mdp(N, c00, c01);
    
    infile.clear();
    infile.seekg(0);
    while (infile >> type) {
        if (type == "A") {
            int i, j; double p, c;
            infile >> i >> j >> p >> c;
            if (i != 0) { // Only load transitions for states != 0
                mdp.add_transition(i, j, p, c);
            }
        } else if (type == "N" || type == "M" || type == "B" || type == "K") {
            double val; infile >> val;
        }
    }
    infile.close();

    mt19937 gen_outer(1234);
    uniform_real_distribution<double> dis_p(0.0, 0.99);

    double best_p = 0.0;
    double best_C = 0.0;
    double min_J = 1e9;

    for (int b = 0; b < B; ++b) {
        double current_p = dis_p(gen_outer);
        mdp.set_p(current_p);
        
        Simulation sim(M, mdp, 42 + b);
        double expected_C = sim.get_expected_cost();
        double J = K_cost * (1.0 - current_p) + expected_C;
        
        if (J < min_J) {
            min_J = J;
            best_p = current_p;
            best_C = expected_C;
        }
    }

    ofstream outfile("results.txt");
    if (!outfile) {
        cerr << "Error opening results.txt" << endl;
        return 1;
    }

    outfile << "2025-11-03-Romolo-Deffereria-2114887\n";
    outfile << "p " << best_p << "\n";
    outfile << "C " << best_C << "\n";
    outfile << "J " << min_J << "\n";

    outfile.close();
    return 0;
}
