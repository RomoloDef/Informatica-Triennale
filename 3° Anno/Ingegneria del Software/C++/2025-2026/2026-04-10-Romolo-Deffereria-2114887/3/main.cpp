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
    double ST0 = params["ST0"];
    double ST1 = params["ST1"];
    double SEP = params["SEP"];
    double SOP = params["SOP"];
    double QEA = params["QEA"];
    double QOA = params["QOA"];

    double total_RR = 0.0;

    for (int m = 0; m < M; ++m) {
        Engine engine(H, 42 + m);

        // Create network with message delay r
        NetworkNode network(&engine, 0, r);
        engine.network = &network;

        // Create servers (1-indexed)
        // Node IDs: servers get IDs 1..S
        std::vector<ServerNode*> servers;
        for (int i = 1; i <= S; ++i) {
            bool is_even = (i % 2 == 0);
            double tauS = is_even ? ST0 : ST1;
            double sep_sop = is_even ? SEP : SOP;
            double qea_qoa = is_even ? QEA : QOA;
            int node_id = i;
            servers.push_back(new ServerNode(&engine, node_id, i, P, Q, tauS, sep_sop, qea_qoa));
        }
        for (int i = 0; i < S; ++i) {
            engine.servers.push_back(servers[i]);
        }

        // Create DB (node_id = S+1)
        DBNode db(&engine, S + 1, P, Q);
        engine.db = &db;

        // Create customers (IDs: S+2, S+3, ...)
        std::vector<Customer*> customers;
        for (int i = 1; i <= C; ++i) {
            customers.push_back(new Customer(&engine, S + 1 + i, A, B, S, P, Q, S0, P0, Q0));
        }

        // Create suppliers (IDs: S+1+C+1, ...)
        std::vector<Supplier*> suppliers;
        for (int i = 1; i <= F; ++i) {
            suppliers.push_back(new Supplier(&engine, S + 1 + C + i, V_param, W, P, Q));
        }

        // Schedule initial events
        for (auto c : customers) c->fire(0.0);
        for (auto f : suppliers) f->fire(0.0);

        // Schedule initial server cache updates
        for (auto sv : servers) sv->scheduleUpdate(0.0);

        // Run simulation
        while (engine.hasEvents()) {
            Event ev = engine.popEvent();

            if (ev.type == EV_CUSTOMER_FIRE) {
                // Find customer by ID
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
                // Server cache update
                if (ev.node_id >= 1 && ev.node_id <= S) {
                    servers[ev.node_id - 1]->doUpdate(ev.time);
                }
            }
        }

        // Compute RR(H) = sum(beta(s,H) - y(s,H)) / H
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

    double expected_RR = total_RR / M;

    std::ofstream outfile("results.txt");
    outfile << "2026-04-10-Romolo-Deffereria-2114887\n";
    outfile << "RR " << expected_RR << "\n";

    return 0;
}
