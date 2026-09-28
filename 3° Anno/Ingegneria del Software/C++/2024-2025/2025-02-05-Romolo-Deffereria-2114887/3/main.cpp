#include <iostream>
#include <fstream>
#include <vector>
#include <random>
#include <string>

using namespace std;

int main() {
    ifstream infile("parameters.txt");
    if (!infile) {
        cerr << "Error opening parameters.txt" << endl;
        return 1;
    }

    vector<vector<double>> transition(3, vector<double>(3));
    for (int i = 0; i < 9; ++i) {
        int u, v;
        double p;
        infile >> u >> v >> p;
        transition[u][v] = p;
    }

    double T1, T2;
    infile >> T1 >> T2;
    infile.close();

    mt19937 gen(42);
    uniform_real_distribution<double> dis(0.0, 1.0);

    int H = 10000;
    int num_simulations = 1000;
    int N_total = 0;

    for (int sim = 0; sim < num_simulations; ++sim) {
        int state = 0;
        double server_available_time = 0.0;
        bool in_session = false;
        double current_session_last_finish = 0.0;

        for (int t = 1; t <= H; ++t) {
            double r = dis(gen);
            int next_state = 0;
            double acc = 0.0;
            for (int j = 0; j < 3; ++j) {
                acc += transition[state][j];
                if (r < acc) {
                    next_state = j;
                    break;
                }
            }

            if (state == 0 && next_state != 0) {
                in_session = true;
            }

            if (next_state != 0) {
                double req_time = (next_state == 1) ? T1 : T2;
                if (server_available_time < t) server_available_time = t;
                server_available_time += req_time;
                if (in_session) {
                    current_session_last_finish = server_available_time;
                }
            }

            if (state != 0 && next_state == 0) {
                if (in_session) {
                    if (current_session_last_finish <= H) {
                        N_total++;
                    }
                    in_session = false;
                }
            }
            state = next_state;
        }
    }

    double avg_N_per_sec = (double)N_total / num_simulations / H;

    ofstream outfile("results.txt");
    if (!outfile) {
        cerr << "Error opening results.txt" << endl;
        return 1;
    }
    
    outfile << "2025-02-05-Romolo-Deffereria-2114887\n";
    outfile << "Avg " << avg_N_per_sec << "\n";
    outfile.close();

    return 0;
}
