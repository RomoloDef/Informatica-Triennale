#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <random>
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
    int Q = params["Q"];
    double V = params["V"];
    double W = params["W"];
    int P = params["P"];
    int S = params["S"];
    int F = params["F"];

    double total_rate = 0;
    
    for (int m = 0; m < M; ++m) {
        Network net;
        for (int i = 1; i <= S; ++i) net.add_server(new Server(i, &net, P, Q));
        for (int i = 1; i <= C; ++i) net.add_customer(new Customer(i, &net, A, B, S, P, Q));
        for (int i = 1; i <= F; ++i) net.add_supplier(new Supplier(i, &net, V, W, S, P, Q));

        for (double time = T; time <= H + 1e-9; time += T) {
            net.step(T);
        }
        double rate = (double)net.get_missed_sales() / H;
        total_rate += rate;
    }

    double expected_rate = total_rate / M;

    std::ofstream out("results.txt");
    out << "2026-01-14-Romolo-Deffereria-2114887\n";
    out << "R " << expected_rate << "\n";
    out.close();

    return 0;
}
