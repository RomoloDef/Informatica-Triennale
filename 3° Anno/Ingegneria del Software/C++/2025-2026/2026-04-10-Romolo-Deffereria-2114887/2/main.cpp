#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <random>
#include <cmath>
#include "network.hpp"
#include "uav.hpp"

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
    int M = static_cast<int>(params["M"]);
    int N = static_cast<int>(params["N"]);
    double L = params["L"];
    double V = params["V"];
    double a = params["a"];
    double b = params["b"];
    double r = params["r"];
    double D = params.count("D") ? params["D"] : 1.0;

    double total_rate = 0.0;

    for (int m = 0; m < M; ++m) {
        std::mt19937 gen(42 + m);
        Network net;
        for (int i = 0; i < N; ++i) {
            net.add_uav(new UAV(i, &net, L, gen));
        }

        // Measure collisions at t=0
        net.measure_collisions(D);

        // Simulation steps
        int steps = static_cast<int>(H / T);
        for (int t = 0; t < steps; ++t) {
            net.step(V, T, a, b, r, gen);
            net.measure_collisions(D);
        }

        double rate = static_cast<double>(net.get_collisions()) / H;
        total_rate += rate;
    }

    double expected_rate = total_rate / M;

    std::ofstream out("results.txt");
    out << "2026-04-10-Romolo-Deffereria-2114887\n";
    out << "C " << expected_rate << "\n";
    out.close();

    return 0;
}
