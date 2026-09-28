#ifndef CUSTOMER_HPP
#define CUSTOMER_HPP

#include "engine.hpp"
#include <vector>
#include <algorithm>

class Customer {
private:
    Engine* engine;
    int id;
    double A, B;
    int S, P, Q;
    double S0, P0, Q0;

    // Helper: select from even or odd indices with given probability
    // prob_even = probability of choosing even class
    // range = 1..max_val
    int selectWithParity(double prob_even, int max_val) {
        std::vector<int> evens, odds;
        for (int idx = 1; idx <= max_val; ++idx) {
            if (idx % 2 == 0) evens.push_back(idx);
            else odds.push_back(idx);
        }

        // If only odds exist, must choose odd
        if (evens.empty()) {
            std::uniform_int_distribution<int> dist(0, odds.size() - 1);
            return odds[dist(engine->getGen())];
        }
        // If only evens exist, must choose even
        if (odds.empty()) {
            std::uniform_int_distribution<int> dist(0, evens.size() - 1);
            return evens[dist(engine->getGen())];
        }

        std::uniform_real_distribution<double> dist01(0.0, 1.0);
        double r = dist01(engine->getGen());
        if (r < prob_even) {
            // Choose even
            std::uniform_int_distribution<int> dist(0, evens.size() - 1);
            return evens[dist(engine->getGen())];
        } else {
            // Choose odd
            std::uniform_int_distribution<int> dist(0, odds.size() - 1);
            return odds[dist(engine->getGen())];
        }
    }

public:
    Customer(Engine* eng, int id, double A, double B, int S, int P, int Q,
             double S0, double P0, double Q0)
        : engine(eng), id(id), A(A), B(B), S(S), P(P), Q(Q),
          S0(S0), P0(P0), Q0(Q0) {}

    void fire(double t) {
        // Stay in state 0 for time tau in [A, B]
        std::uniform_real_distribution<double> dist_tau(A, B);
        double tau = dist_tau(engine->getGen());

        // Schedule next fire
        engine->schedule(t + tau, EV_CUSTOMER_FIRE, id);

        // Choose server s with parity-based probability
        int s = selectWithParity(S0, S);

        // Choose product i with parity-based probability
        int i = selectWithParity(P0, P);

        // Choose quantity q with parity-based probability
        int q = selectWithParity(Q0, Q);

        // Send request (i, q) to server s through network
        Message out;
        out.dst_type = TYPE_NETWORK;
        out.dst_id = 0;
        out.msg_type = MSG_CUST_TO_SERVER;
        out.c = id;
        out.s = s;
        out.i = i;
        out.q = q;
        // The network will route this; we set final destination info
        // Actually, let the network forward it. We store actual dest in the message.
        // The network needs to know where to forward.
        // Let's use dst_type as the FINAL destination (after network)
        out.dst_type = TYPE_SERVER;
        out.dst_id = s;

        // But messages must pass through network first - send to network
        engine->network->push(out, t);
    }
};

#endif
