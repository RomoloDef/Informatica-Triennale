#include "engine.hpp"
#include "network.hpp"
#include "server.hpp"
#include "customer.hpp"
#include "supplier.hpp"
#include <iostream>
#include <fstream>
#include <string>
#include <map>

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
    int P = static_cast<int>(params["P"]);
    int W = static_cast<int>(params["W"]);
    double a1 = params["a1"];
    double a2 = params["a2"];
    double a3 = params["a3"];
    double a4 = params["a4"];
    double a5 = params["a5"];
    double b1 = params["b1"];
    double b2 = params["b2"];
    double b3 = params["b3"];
    double b4 = params["b4"];
    double b5 = params["b5"];
    double r = params["r"];
    double tau0 = params["tau0"];
    double tau1 = params["tau1"];

    double total_RR = 0.0;

    for (int m = 0; m < M; ++m) {
        Engine engine(H, 42 + m);

        NetworkNode network(&engine, 0, r);
        engine.network = &network;

        ServerNode server(&engine, 1, P, W, tau0, tau1, b5);
        engine.server = &server;

        std::vector<Customer*> customers;
        for (int i = 1; i <= P; ++i) {
            customers.push_back(new Customer(&engine, 1 + i, i, a1, b1, a2, b2, a3, b3, a4, b4));
        }
        engine.customers = customers;

        std::vector<Supplier*> suppliers;
        for (int i = 1; i <= P; ++i) {
            suppliers.push_back(new Supplier(&engine, 1 + P + i, a5, b5));
        }
        engine.suppliers = suppliers;

        // Schedule initial customer fires
        for (auto c : customers) {
            c->fire(0.0);
        }

        // Schedule initial server update
        server.scheduleUpdate(0.0);

        // Run simulation
        while (engine.hasEvents()) {
            Event ev = engine.popEvent();

            if (ev.type == EV_CUSTOMER_FIRE) {
                // Find customer by node id (which is 1 + i)
                int prod_id = ev.node_id - 1;
                customers[prod_id - 1]->fire(ev.time);
            } else if (ev.type == EV_SERVER_UPDATE) {
                server.doUpdate(ev.time);
            } else if (ev.type == EV_NODE_FINISH) {
                if (ev.node_id == 0) {
                    network.processFinish(ev.time);
                } else if (ev.node_id == 1) {
                    server.processFinish(ev.time);
                } else if (ev.node_id > 1 && ev.node_id <= 1 + P) {
                    customers[ev.node_id - 1 - 1]->processFinish(ev.time);
                } else {
                    suppliers[ev.node_id - 1 - P - 1]->processFinish(ev.time);
                }
            }
        }

        double RR = server.getSellBuy() / H;
        total_RR += RR;

        for (auto c : customers) delete c;
        for (auto s : suppliers) delete s;
    }

    double expected_RR = total_RR / M;

    std::ofstream outfile("results.txt");
    outfile << "2026-06-23-Romolo-Deffereria-2114887\n";
    outfile << "RR " << expected_RR << "\n";

    return 0;
}
