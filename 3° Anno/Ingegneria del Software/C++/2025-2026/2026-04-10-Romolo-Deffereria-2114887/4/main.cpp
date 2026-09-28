#include "engine.hpp"
#include "network.hpp"
#include "server.hpp"
#include "db.hpp"
#include "customer.hpp"
#include "supplier.hpp"
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <cmath>
#include <random>
#include <limits>

// Function that runs the simulation with given ST0, ST1 and returns mean RR
double runSimulation(double H, int M, int C, int S, int F, int P, int Q,
                     double A, double B, double V_param, double W,
                     double r, double S0, double P0, double Q0,
                     double ST0, double ST1,
                     double SEP, double SOP, double QEA, double QOA) {
    double total_RR = 0.0;

    for (int m = 0; m < M; ++m) {
        Engine engine(H, 42 + m);

        NetworkNode network(&engine, 0, r);
        engine.network = &network;

        std::vector<ServerNode*> servers;
        for (int i = 1; i <= S; ++i) {
            bool is_even = (i % 2 == 0);
            double tauS = is_even ? ST0 : ST1;
            double sep_sop = is_even ? SEP : SOP;
            double qea_qoa = is_even ? QEA : QOA;
            servers.push_back(new ServerNode(&engine, i, i, P, Q, tauS, sep_sop, qea_qoa));
        }
        for (int i = 0; i < S; ++i) {
            engine.servers.push_back(servers[i]);
        }

        DBNode db(&engine, S + 1, P, Q);
        engine.db = &db;

        std::vector<Customer*> customers;
        for (int i = 1; i <= C; ++i) {
            customers.push_back(new Customer(&engine, S + 1 + i, A, B, S, P, Q, S0, P0, Q0));
        }

        std::vector<Supplier*> suppliers;
        for (int i = 1; i <= F; ++i) {
            suppliers.push_back(new Supplier(&engine, S + 1 + C + i, V_param, W, P, Q));
        }

        for (auto c : customers) c->fire(0.0);
        for (auto f : suppliers) f->fire(0.0);
        for (auto sv : servers) sv->scheduleUpdate(0.0);

        while (engine.hasEvents()) {
            Event ev = engine.popEvent();

            if (ev.type == EV_CUSTOMER_FIRE) {
                int cust_idx = ev.node_id - S - 1 - 1;
                if (cust_idx >= 0 && cust_idx < C) {
                    customers[cust_idx]->fire(ev.time);
                }
            } else if (ev.type == EV_SUPPLIER_FIRE) {
                int supp_idx = ev.node_id - S - 1 - C - 1;
                if (supp_idx >= 0 && supp_idx < F) {
                    suppliers[supp_idx]->fire(ev.time);
                }
            } else if (ev.type == EV_NODE_FINISH) {
                if (ev.node_id == 0) {
                    network.processFinish(ev.time);
                } else if (ev.node_id >= 1 && ev.node_id <= S) {
                    servers[ev.node_id - 1]->processFinish(ev.time);
                } else if (ev.node_id == S + 1) {
                    db.processFinish(ev.time);
                }
            } else if (ev.type == EV_SERVER_UPDATE) {
                if (ev.node_id >= 1 && ev.node_id <= S) {
                    servers[ev.node_id - 1]->doUpdate(ev.time);
                }
            }
        }

        double sum_beta_minus_y = 0.0;
        for (auto sv : servers) {
            sum_beta_minus_y += sv->getSellBuy() - sv->getY();
        }
        double RR = sum_beta_minus_y / H;
        total_RR += RR;

        for (auto s_ptr : servers) delete s_ptr;
        for (auto c_ptr : customers) delete c_ptr;
        for (auto f_ptr : suppliers) delete f_ptr;
    }

    return total_RR / M;
}

int main() {
    std::map<std::string, double> params;
    std::ifstream infile("parameters.txt");
    std::string key;
    double value;
    while (infile >> key >> value) {
        params[key] = value;
    }

    double H = params["H"];
    int M = static_cast<int>(params["M"]);
    int C = static_cast<int>(params["C"]);
    int S = static_cast<int>(params["S"]);
    int F = static_cast<int>(params["F"]);
    int P = static_cast<int>(params["P"]);
    int Q = static_cast<int>(params["Q"]);

    double A = params["A"];
    double B = params["B"];
    double V_param = params["V"];
    double W = params["W"];

    double r = params["r"];
    double S0 = params["S0"];
    double P0 = params["P0"];
    double Q0 = params["Q0"];
    double SEP = params["SEP"];
    double SOP = params["SOP"];
    double QEA = params["QEA"];
    double QOA = params["QOA"];

    double a_val = params["a"];
    double b_val = params["b"];
    int G = static_cast<int>(params["G"]);

    double best_RR = -std::numeric_limits<double>::max();
    std::vector<std::pair<double,double>> best_pairs;

    for (int k0 = 0; k0 <= G; ++k0) {
        double st0 = a_val + k0 * (b_val - a_val) / G;
        for (int k1 = 0; k1 <= G; ++k1) {
            double st1 = a_val + k1 * (b_val - a_val) / G;

            double rr = runSimulation(H, M, C, S, F, P, Q,
                                      A, B, V_param, W,
                                      r, S0, P0, Q0,
                                      st0, st1,
                                      SEP, SOP, QEA, QOA);

            if (best_pairs.empty() || rr > best_RR + 1e-9) {
                best_RR = rr;
                best_pairs.clear();
                best_pairs.push_back({st0, st1});
            } else if (std::abs(rr - best_RR) <= 1e-9) {
                best_pairs.push_back({st0, st1});
            }
        }
    }

    // Select one optimum at random
    std::mt19937 rng(12345);
    int chosen_idx = 0;
    if (best_pairs.size() > 1) {
        std::uniform_int_distribution<int> dist(0, best_pairs.size() - 1);
        chosen_idx = dist(rng);
    }
    double opt_ST0 = best_pairs[chosen_idx].first;
    double opt_ST1 = best_pairs[chosen_idx].second;

    std::ofstream outfile("results.txt");
    outfile << "2026-04-10-Romolo-Deffereria-2114887\n";
    outfile << "RR " << best_RR << "\n";
    outfile << "ST0 " << opt_ST0 << "\n";
    outfile << "ST1 " << opt_ST1 << "\n";

    return 0;
}
