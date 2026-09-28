#ifndef SUPPLIER_HPP
#define SUPPLIER_HPP

#include "engine.hpp"

class Supplier {
private:
    Engine* engine;
    int id;
    double V_param;
    double W;
    int P;
    int Q;

public:
    Supplier(Engine* eng, int id, double V_param, double W, int P, int Q)
        : engine(eng), id(id), V_param(V_param), W(W), P(P), Q(Q) {}
        
    void fire(double t) {
        std::uniform_real_distribution<double> dist_gamma(V_param, W);
        double gamma = dist_gamma(engine->getGen());
        
        engine->schedule(t + gamma, EV_SUPPLIER_FIRE, id);
        
        std::uniform_int_distribution<int> dist_p(1, P);
        std::uniform_int_distribution<int> dist_q(1, Q);
        
        int i = dist_p(engine->getGen());
        int q = dist_q(engine->getGen());
        
        Message out;
        out.dst_type = TYPE_DB;
        out.dst_id = 0;
        out.msg_type = MSG_SUPP_RESTOCK;
        out.i = i;
        out.q = q;
        
        engine->route(out, t);
    }
};

#endif
