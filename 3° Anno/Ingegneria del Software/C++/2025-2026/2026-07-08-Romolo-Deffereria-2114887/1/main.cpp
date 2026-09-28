#include "network.hpp"
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <cmath>

int main() {
    std::map<std::string, double> params;
    std::ifstream infile("parameters.txt");
    std::string key;
    double value;
    while (infile >> key >> value) {
        params[key] = value;
    }

    double T = params["T"];
    double H = params["H"];
    int M = static_cast<int>(params["M"]);
    int N = static_cast<int>(params["N"]);
    double L = params["L"];
    double V = params["V"];
    double r = params["r"];
    double PFAIL = params["PFAIL"];
    double PREC = params["PREC"];
    int K = static_cast<int>(params["K"]);

    int steps = static_cast<int>(std::floor(H / T));

    double total_AVGC = 0.0;

    for (int m = 0; m < M; ++m) {
        std::mt19937 gen(42 + m);
        Network net;
        net.init(N, K, L, gen);

        double sum_S = 0.0;

        sum_S += net.stdDevCoverage(r);

        for (int s = 0; s < steps; ++s) {
            net.step(V, T, PFAIL, PREC, gen);
            sum_S += net.stdDevCoverage(r);
        }

        double AVGS = sum_S / steps;
        double AVGC = (1.0 / N) * AVGS;
        total_AVGC += AVGC;
    }

    double expected_AVGC = total_AVGC / M;

    std::ofstream outfile("results.txt");
    outfile << "2026-07-08-Romolo-Deffereria-2114887" << "\n";
    outfile << "AVGC " << expected_AVGC << "\n";

    return 0;
}
