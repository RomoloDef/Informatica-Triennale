#include <iostream>
#include <fstream>
#include <vector>
#include <random>
#include <queue>
#include <cmath>

using namespace std;

struct Server {
    vector<int> cache;
    vector<int> local_sales;
    int busy_timer;
    queue<int> fifo;
};

int main() {
    ifstream infile("parameters.txt");
    if (!infile) {
        cerr << "Error opening parameters.txt" << endl;
        return 1;
    }

    int H, n, k;
    double alpha;
    infile >> H >> n >> k >> alpha;

    vector<double> p(k + 1);
    for (int i = 0; i <= k; ++i) {
        infile >> p[i];
    }

    vector<double> f(k + 1);
    for (int i = 0; i <= k; ++i) {
        infile >> f[i];
    }
    infile.close();

    mt19937 gen(42);
    uniform_real_distribution<double> dis(0.0, 1.0);

    int num_simulations = 1000;
    long long total_transactions = 0;

    for (int sim = 0; sim < num_simulations; ++sim) {
        vector<int> central_DB(k + 1, 0);
        vector<Server> servers(n + 1);
        for (int s = 1; s <= n; ++s) {
            servers[s].cache.assign(k + 1, 0);
            servers[s].local_sales.assign(k + 1, 0);
            servers[s].busy_timer = 0;
            while (!servers[s].fifo.empty()) servers[s].fifo.pop();
        }

        int transactions = 0;

        for (int t = 1; t <= H; ++t) {
            // Provider
            double r_f = dis(gen);
            int req_f = 0;
            double acc_f = 0;
            for (int i = 0; i <= k; ++i) {
                acc_f += f[i];
                if (r_f < acc_f) { req_f = i; break; }
            }
            if (req_f != 0) {
                central_DB[req_f]++;
            }

            // Customers
            for (int s = 1; s <= n; ++s) {
                double r_p = dis(gen);
                int req_p = 0;
                double acc_p = 0;
                for (int i = 0; i <= k; ++i) {
                    acc_p += p[i];
                    if (r_p < acc_p) { req_p = i; break; }
                }
                if (req_p != 0) {
                    if (servers[s].fifo.size() < 1000) {
                        servers[s].fifo.push(req_p);
                    }
                }
            }

            // Servers
            for (int s = 1; s <= n; ++s) {
                if (servers[s].busy_timer > 0) {
                    servers[s].busy_timer--;
                    continue;
                }
                
                if (!servers[s].fifo.empty()) {
                    int prod = servers[s].fifo.front();
                    servers[s].fifo.pop();
                    transactions++;
                    
                    if (servers[s].cache[prod] - servers[s].local_sales[prod] > 0) {
                        servers[s].local_sales[prod]++;
                        
                        double r_alpha = dis(gen);
                        if (r_alpha < alpha) {
                            servers[s].busy_timer = 10;
                            for (int i = 1; i <= k; ++i) {
                                central_DB[i] -= servers[s].local_sales[i];
                                if (central_DB[i] < 0) {
                                    central_DB[i] = 0;
                                }
                                servers[s].local_sales[i] = 0;
                                servers[s].cache[i] = central_DB[i];
                            }
                        }
                    }
                }
            }
        }
        total_transactions += transactions;
    }

    double Z = (double)total_transactions / num_simulations;
    double W = Z / (n * H);

    ofstream outfile("results.txt");
    if (!outfile) {
        cerr << "Error opening results.txt" << endl;
        return 1;
    }
    
    outfile << "2025-03-21-Romolo-Deffereria-2114887\n";
    outfile << "Z " << Z << "\n";
    outfile << "W " << W << "\n";
    outfile.close();

    return 0;
}
