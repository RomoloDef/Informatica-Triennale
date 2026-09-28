#include "Customer.hpp"
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
    double H, A, B, T;
    int N;

    infile >> dump >> H;
    infile >> dump >> N;
    infile >> dump >> A;
    infile >> dump >> B;
    infile >> dump >> T;
    infile.close();

    ofstream outfile("results.txt");
    if (!outfile) {
        cerr << "Error opening results.txt" << endl;
        return 1;
    }

    outfile << "2025-06-12-Romolo-Deffereria-2114887\n";

    Customer customer(N, A, B, 42);

    double current_time = 0.0;
    while (current_time <= H + 1e-9) {
        int output = 0;
        if (current_time == 0.0) {
            // For t=0, we call step with T=0 to just get the initial request
            output = customer.step(0.0);
        } else {
            output = customer.step(T);
        }
        
        outfile << current_time << " " << output << "\n";
        current_time += T;
    }

    outfile.close();
    return 0;
}
