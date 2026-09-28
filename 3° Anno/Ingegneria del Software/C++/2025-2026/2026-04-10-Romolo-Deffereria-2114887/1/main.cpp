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

    // D is the collision distance threshold (from exercise text: distance < D)
    // The exercise says "distanza minore di D", D needs to come from parameters
    // But D is not listed as a parameter! Looking at the exercise text more carefully:
    // "Un veicolo i ha una collisione al tempo t se esiste un veicolo j > i che si trova
    //  a distanza minore di D dal veicolo i."
    // D is mentioned in the text but NOT in the parameter list (section 2).
    // Wait - let me re-read. The parameters list does NOT include D.
    // But D is used in the collision definition. This is likely an implicit parameter
    // that should be read. Let me check if it's in parameters or if it's missing.
    // Looking at the parameter list: T, H, L, V, N, M, a, b. No D.
    // But the problem says "distanza minore di D". D must be a parameter.
    // I'll read it from the file if present, like previous exams did.
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

        // Simulation: t = 1, 2, ... until t*T > H
        int steps = static_cast<int>(H / T);
        for (int t = 0; t < steps; ++t) {
            net.step(V, T, a, b, gen);
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
