#include "Customer.hpp"

Customer::Customer(int n, double a, double b, int seed)
    : N(n), A(a), B(b), gen(seed), tau(0.0), time_since_last_req(0.0) {}

int Customer::step(double T) {
    time_since_last_req += T;
    
    // If it's the very first step (tau == 0.0) or enough time has passed
    if (tau == 0.0 || time_since_last_req >= tau) {
        std::uniform_real_distribution<double> dis_tau(A, B);
        std::uniform_int_distribution<int> dis_prod(1, N);
        
        tau = dis_tau(gen);
        time_since_last_req = 0.0;
        return dis_prod(gen);
    }
    
    return 0;
}
