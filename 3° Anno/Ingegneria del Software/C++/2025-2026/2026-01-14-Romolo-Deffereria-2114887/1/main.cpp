#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <random>
#include <cmath>
#include "Network.hpp"
#include "UAV.hpp"

std::mt19937 gen(42);
std::uniform_real_distribution<double> dist_unif(0.0, 1.0);

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
    int N = params["N"];
    double L = params["L"];
    double V = params["V"];
    double A = params["A"];
    double D = params["D"];
    double R = params["R"];

    double total_rate = 0;
    
    for (int m = 0; m < M; ++m) {
        Network net;
        for (int i = 0; i < N; ++i) {
            net.add_uav(new UAV(i, &net, L));
        }

        double next_measure = R;
        for (double time = T; time <= H + 1e-9; time += T) {
            net.step(A, L, V, T);
            if (time >= next_measure - 1e-9) {
                net.measure_collisions(D);
                next_measure += R;
            }
        }
        double rate = (double)net.get_collisions() / H;
        total_rate += rate;
    }

    double expected_rate = total_rate / M;

    std::ofstream out("results.txt");
    out << "2026-01-14-Romolo-Deffereria-2114887\n";
    out << "C " << expected_rate << "\n";
    out.close();

    return 0;
}
