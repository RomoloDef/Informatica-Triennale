#ifndef CUSTOMER_HPP
#define CUSTOMER_HPP

#include "engine.hpp"

class Customer {
private:
    Engine* engine;
    int id;
    double A;
    double B;
    int S;
    int P;
    int Q;

public:
    Customer(Engine* eng, int id, double A, double B, int S, int P, int Q)
        : engine(eng), id(id), A(A), B(B), S(S), P(P), Q(Q) {}
        
    void fire(double t) {
        std::uniform_real_distribution<double> dist_tau(A, B);
        double tau = dist_tau(engine->getGen());
        
        engine->schedule(t + tau, EV_CUSTOMER_FIRE, id);
        
        std::uniform_int_distribution<int> dist_s(1, S);
        std::uniform_int_distribution<int> dist_p(1, P);
        std::uniform_int_distribution<int> dist_q(1, Q);
        
        int s = dist_s(engine->getGen());
        int i = dist_p(engine->getGen());
        int q = dist_q(engine->getGen());
        
        Message out;
        out.dst_type = TYPE_SERVER;
        out.dst_id = s;
        out.msg_type = MSG_CUST_REQ;
        out.c = id;
        out.s = s;
        out.i = i;
        out.q = q;
        
        engine->route(out, t);
    }
};

#endif
