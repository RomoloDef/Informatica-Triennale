#include "Simulation.hpp"
#include <iostream>
#include <string>

using namespace std;

int main() {
    ifstream infile("parameters.txt");
    if (!infile) {
        cerr << "Error opening parameters.txt" << endl;
        return 1;
    }

    string dump;
    double H, V, T;
    int N;

    infile >> dump >> H;
    infile >> dump >> N;
    infile >> dump >> V;
    infile >> dump >> T;
    infile.close();

    ofstream outfile("results.txt");
    if (!outfile) {
        cerr << "Error opening results.txt" << endl;
        return 1;
    }

    outfile << "2025-06-12-Romolo-Deffereria-2114887\n";

    Simulation sim(H, N, V, T, outfile);
    sim.run();

    outfile.close();
    return 0;
}
