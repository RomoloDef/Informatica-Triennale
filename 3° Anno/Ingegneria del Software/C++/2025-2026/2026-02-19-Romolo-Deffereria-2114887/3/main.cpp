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
    
    double H = params.count("H") ? params["H"] : 234.6;
    int M = params.count("M") ? static_cast<int>(params["M"]) : 100;
    int C = params.count("C") ? static_cast<int>(params["C"]) : 10;
    int S = params.count("S") ? static_cast<int>(params["S"]) : 4;
    int F = params.count("F") ? static_cast<int>(params["F"]) : 2;
    int P = params.count("P") ? static_cast<int>(params["P"]) : 10;
    int Q = params.count("Q") ? static_cast<int>(params["Q"]) : 3;
    
    double A = params.count("A") ? params["A"] : 1.0;
    double B = params.count("B") ? params["B"] : 2.0;
    double V_param = params.count("V") ? params["V"] : 3.0;
    double W = params.count("W") ? params["W"] : 5.0;
    
    double r = params.count("r") ? params["r"] : 0.01;
    double w = params.count("w") ? params["w"] : 0.01;
    double l = params.count("l") ? params["l"] : 3.1;
    double s = params.count("s") ? params["s"] : 6.3;
    double z = params.count("z") ? params["z"] : 0.1;
    double v_write = params.count("v") ? params["v"] : 0.2;
    
    double total_rate_sum = 0.0;
    
    for (int m = 0; m < M; ++m) {
        Engine engine(H, 42 + m); // vary seed per monte carlo run
        
        NetworkNode network(&engine, 0, r, w);
        engine.network = &network;
        
        std::vector<ServerNode*> servers;
        for (int i = 1; i <= S; ++i) {
            servers.push_back(new ServerNode(&engine, i, z, v_write));
        }
        for (int i = 0; i < S; ++i) engine.servers.push_back(servers[i]);
        
        DBNode db(&engine, S + 1, l, s, P, Q);
        engine.db = &db;
        
        std::vector<Customer*> customers;
        for (int i = 1; i <= C; ++i) {
            customers.push_back(new Customer(&engine, S + 1 + i, A, B, S, P, Q));
        }
        
        std::vector<Supplier*> suppliers;
        for (int i = 1; i <= F; ++i) {
            suppliers.push_back(new Supplier(&engine, S + 1 + C + i, V_param, W, P, Q));
        }
        
        // Initial events
        for (auto c : customers) c->fire(0.0);
        for (auto f : suppliers) f->fire(0.0);
        
        while (engine.hasEvents()) {
            Event ev = engine.popEvent();
            if (ev.type == EV_CUSTOMER_FIRE) {
                customers[ev.node_id - S - 1 - 1]->fire(ev.time);
            } else if (ev.type == EV_SUPPLIER_FIRE) {
                suppliers[ev.node_id - S - 1 - C - 1]->fire(ev.time);
            } else if (ev.type == EV_NODE_FINISH) {
                if (ev.node_id == 0) {
                    network.processFinish(ev.time);
                } else if (ev.node_id >= 1 && ev.node_id <= S) {
                    servers[ev.node_id - 1]->processFinish(ev.time);
                } else if (ev.node_id == S + 1) {
                    db.processFinish(ev.time);
                }
            }
        }
        
        double run_rate = engine.total_transactions > 0 ? (static_cast<double>(engine.total_missed_sales) / engine.total_transactions) : 0.0;
        total_rate_sum += run_rate;
        
        for (auto s_ptr : servers) delete s_ptr;
        for (auto c_ptr : customers) delete c_ptr;
        for (auto f_ptr : suppliers) delete f_ptr;
    }
    
    double expected_rate = total_rate_sum / M;
    
    std::ofstream outfile("results.txt");
    outfile << "2026-02-19-Romolo-Deffereria-2114887\n";
    outfile << "R " << expected_rate << "\n";
    
    return 0;
}
