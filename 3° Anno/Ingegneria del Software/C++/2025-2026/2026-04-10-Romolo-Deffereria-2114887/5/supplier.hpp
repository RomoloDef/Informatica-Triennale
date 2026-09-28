#ifndef SUPPLIER_HPP
#define SUPPLIER_HPP

#include "engine.hpp"

class Supplier {
private:
    Engine* engine;
    int id;
    double V_param; // min sojourn time
    double W;       // max sojourn time
    int P;          // number of products
    int Q;          // max quantity

public:
    Supplier(Engine* eng, int id, double V_param, double W, int P, int Q)
        : engine(eng), id(id), V_param(V_param), W(W), P(P), Q(Q) {}

    void fire(double t) {
        // Stay in state 0 for time gamma in [V, W]
        std::uniform_real_distribution<double> dist_gamma(V_param, W);
        double gamma = dist_gamma(engine->getGen());

        // Schedule next fire
        engine->schedule(t + gamma, EV_SUPPLIER_FIRE, id);

        // Choose product i uniformly in {1, ..., P}
        std::uniform_int_distribution<int> dist_p(1, P);
        int i = dist_p(engine->getGen());

        // Choose quantity q uniformly in {1, ..., Q}
        std::uniform_int_distribution<int> dist_q(1, Q);
        int q = dist_q(engine->getGen());

        // Send (i, q) to DB through network
        Message out;
        out.dst_type = TYPE_DB;
        out.dst_id = 0;
        out.msg_type = MSG_SUPPLIER_TO_DB;
        out.i = i;
        out.q = q;

        engine->network->push(out, t);
    }
};

#endif
