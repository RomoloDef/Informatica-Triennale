#include "engine.hpp"
#include "network.hpp"
#include "server.hpp"
#include "customer.hpp"
#include "supplier.hpp"
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <limits>
#include <vector>
#include <utility>
#include <future>

double runSimulation(double H, int M, int P, int W, double a1, double a2, double a3, double a4, double a5,
                     double b1, double b2, double b3, double b4, double b5, double r, double tau0, double tau1) {
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

        for (auto c : customers) c->fire(0.0);
        server.scheduleUpdate(0.0);

        while (engine.hasEvents()) {
            Event ev = engine.popEvent();

            if (ev.type == EV_CUSTOMER_FIRE) {
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

    double best_RR = -std::numeric_limits<double>::max();
    std::vector<std::pair<int, int> > best_xy;

    for (int x = 0; x <= 100; ++x) {
        std::vector<std::future<double>> futures(101);
        for (int y = 0; y <= 100; ++y) {
            double tau0 = (a1 + b1) * W * (x / 100.0);
            double tau1 = (a2 + b2 * P) * W * (y / 100.0);
            futures[y] = std::async(std::launch::async, runSimulation, H, M, P, W, a1, a2, a3, a4, a5, b1, b2, b3, b4, b5, r, tau0, tau1);
        }

        for (int y = 0; y <= 100; ++y) {
            double rr = futures[y].get();
            if (best_xy.empty() || rr > best_RR + 1e-9) {
                best_RR = rr;
                best_xy.clear();
                best_xy.push_back(std::make_pair(x, y));
            } else if (std::abs(rr - best_RR) <= 1e-9) {
                best_xy.push_back(std::make_pair(x, y));
            }
        }
    }

    // Select one optimal combination uniformly at random
    std::mt19937 rng(12345);
    int chosen_x = 0, chosen_y = 0;
    if (best_xy.size() == 1) {
        chosen_x = best_xy[0].first;
        chosen_y = best_xy[0].second;
    } else {
        std::uniform_int_distribution<int> dist(0, best_xy.size() - 1);
        int idx = dist(rng);
        chosen_x = best_xy[idx].first;
        chosen_y = best_xy[idx].second;
    }

    double opt_tau0 = (a1 + b1) * W * (chosen_x / 100.0);
    double opt_tau1 = (a2 + b2 * P) * W * (chosen_y / 100.0);

    std::ofstream outfile("results.txt");
    outfile << "2026-06-23-Romolo-Deffereria-2114887\n";
    outfile << "RR " << best_RR << "\n";
    outfile << "x " << chosen_x << "\n";
    outfile << "y " << chosen_y << "\n";
    outfile << "tau0 " << opt_tau0 << "\n";
    outfile << "tau1 " << opt_tau1 << "\n";

    return 0;
}
