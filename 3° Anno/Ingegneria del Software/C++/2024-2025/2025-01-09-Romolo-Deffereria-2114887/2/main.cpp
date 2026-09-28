#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <random>

using namespace std;

struct Edge {
    int dest;
    double prob;
    double cost;
};

int main() {
    ifstream infile("parameters.txt");
    if (!infile) {
        cerr << "Error opening parameters.txt" << endl;
        return 1;
    }

    string C_str;
    double max_C;
    infile >> C_str >> max_C;

    string N_str;
    int N;
    infile >> N_str >> N;

    vector<vector<Edge>> adj(N);

    string A_str;
    int u, v;
    double prob, cost;
    while (infile >> A_str >> u >> v >> prob >> cost) {
        adj[u].push_back({v, prob, cost});
    }
    infile.close();

    mt19937 gen(42);
    uniform_real_distribution<double> dis(0.0, 1.0);

    int num_simulations = 1000;
    int count_success = 0;

    for (int s = 0; s < num_simulations; ++s) {
        int current_state = 0;
        double current_cost = 0.0;

        while (current_state != N - 1) {
            double r = dis(gen);
            double acc = 0.0;
            int next_state = current_state;
            for (const auto& edge : adj[current_state]) {
                acc += edge.prob;
                if (r < acc) {
                    current_cost += edge.cost;
                    next_state = edge.dest;
                    break;
                }
            }
            if (next_state == current_state) {
                break;
            }
            current_state = next_state;
        }
        if (current_cost <= max_C) {
            count_success++;
        }
    }

    double prob_success = static_cast<double>(count_success) / num_simulations;

    ofstream outfile("results.txt");
    if (!outfile) {
        cerr << "Error opening results.txt" << endl;
        return 1;
    }
    outfile << "2025-01-09-Romolo-Deffereria-2114887\n";
    outfile << "P " << prob_success << "\n";
    outfile.close();

    return 0;
}
