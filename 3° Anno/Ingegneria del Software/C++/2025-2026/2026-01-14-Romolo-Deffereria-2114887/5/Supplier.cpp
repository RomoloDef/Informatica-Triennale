#include "Supplier.hpp"
#include "Network.hpp"
#include <random>

extern std::mt19937 gen;

Supplier::Supplier(int id, Network* net, double V, double W, int S, int P, int Q)
    : id(id), net(net), V(V), W(W), S(S), P(P), Q(Q) {
    std::uniform_real_distribution<double> dist(V, W);
    timer = dist(gen);
}

void Supplier::update(double T) {
    timer -= T;
    while (timer <= 0) {
        std::uniform_int_distribution<int> dist_s(1, S);
        std::uniform_int_distribution<int> dist_p(1, P);
        std::uniform_int_distribution<int> dist_q(1, Q);
        
        int s = dist_s(gen);
        int i = dist_p(gen);
        int q = dist_q(gen);
        
        net->send_supplier_req(id, s, i, q);
        
        std::uniform_real_distribution<double> dist(V, W);
        timer += dist(gen);
    }
}
