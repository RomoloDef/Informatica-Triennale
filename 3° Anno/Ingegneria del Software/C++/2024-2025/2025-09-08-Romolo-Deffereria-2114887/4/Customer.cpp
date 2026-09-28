#include "Customer.hpp"

Customer::Customer(double a, double b, int s, int p, int seed)
    : A(a), B(b), S(s), P(p), gen(seed), tau(0.0), time_since_last_req(0.0), missed_sales(0) {}

std::pair<int, int> Customer::step(double T) {
    time_since_last_req += T;
    
    if (tau == 0.0 || time_since_last_req >= tau) {
        std::uniform_real_distribution<double> dis_tau(A, B);
        std::uniform_int_distribution<int> dis_server(1, S);
        std::uniform_int_distribution<int> dis_prod(1, P);
        
        tau = dis_tau(gen);
        time_since_last_req = 0.0;
        
        return {dis_server(gen), dis_prod(gen)};
    }
    
    return {0, 0};
}

void Customer::receive_response(int msg) {
    if (msg < 0) {
        missed_sales++;
    }
}
