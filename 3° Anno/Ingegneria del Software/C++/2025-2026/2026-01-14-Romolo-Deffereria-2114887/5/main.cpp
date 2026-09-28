#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <random>
#include <limits>
#include "Network.hpp"
#include "Customer.hpp"
#include "Supplier.hpp"
#include "Server.hpp"

std::mt19937 gen(42);

int main() {
    std::ifstream in("parameters.txt");
    if (!in) {
        std::cerr << "Error opening parameters.txt\n";
        return 1;
    }

    std::map<std::string, double> params;
    std::string key;
    double val;
    while (in >> key >> val) {
        params[key] = val;
    }

    double T = params["T"];
    double H = params["H"];
    int M = params["M"];
    int C = params["C"];
    double A = params["A"];
    double B = params["B"];
    int G = params["G"];
    int F = params["F"];
    
    // Q is missing in the example parameters.txt due to a likely typo in the exam text 
    // ("V e Q sono omesse" vs "V e W non sono presenti"). 
    // We will use 5 as a default, or read it if it's there.
    int Q = params.count("Q") ? params["Q"] : 5;
    
    int P = params["P"];
    int S = params["S"];
    double a = params["a"];
    double b = params["b"];

    double min_J = std::numeric_limits<double>::infinity();
    double best_V = 1;
    double best_W = 6;
    double best_R = 0;

    for (int v_int = 1; v_int <= G; ++v_int) {
        double V_val = (double)v_int;
        double W_val = V_val + 5.0;
        double total_rate = 0;
        for (int m = 0; m < M; ++m) {
            Network net;
            for (int i = 1; i <= S; ++i) net.add_server(new Server(i, &net, P, Q));
            for (int i = 1; i <= C; ++i) net.add_customer(new Customer(i, &net, A, B, S, P, Q));
            for (int i = 1; i <= F; ++i) net.add_supplier(new Supplier(i, &net, V_val, W_val, S, P, Q));

            for (double time = T; time <= H + 1e-9; time += T) {
                net.step(T);
            }
            double rate = (double)net.get_missed_sales() / H;
            total_rate += rate;
        }
        double R_val = total_rate / M;
        double J = a * V_val + b * R_val;
        if (J < min_J) {
            min_J = J;
            best_V = V_val;
            best_W = W_val;
            best_R = R_val;
        }
    }

    std::ofstream out("results.txt");
    out << "2026-01-14-Romolo-Deffereria-2114887\n";
    out << "R " << best_R << "\n";
    out << "V " << best_V << "\n";
    out << "W " << best_W << "\n";
    out << "J " << min_J << "\n";
    out.close();

    return 0;
}
