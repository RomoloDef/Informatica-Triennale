#include "Customer.hpp"
#include "Network.hpp"
#include <random>

extern std::mt19937 gen;

Customer::Customer(int id, Network* net, double A, double B, int S, int P, int Q)
    : id(id), net(net), A(A), B(B), S(S), P(P), Q(Q) {
    std::uniform_real_distribution<double> dist(A, B);
    timer = dist(gen);
}

void Customer::update(double T) {
    timer -= T;
    while (timer <= 0) {
        std::uniform_int_distribution<int> dist_s(1, S);
        std::uniform_int_distribution<int> dist_p(1, P);
        std::uniform_int_distribution<int> dist_q(1, Q);
        
        int s = dist_s(gen);
        int i = dist_p(gen);
        int q = dist_q(gen);
        
        net->send_customer_req(id, s, i, q);
        
        std::uniform_real_distribution<double> dist(A, B);
        timer += dist(gen);
    }
}
