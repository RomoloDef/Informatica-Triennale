#include "Customer.hpp"

Customer::Customer(int n, int s, double a, double b, int seed)
    : N(n), S(s), A(a), B(b), gen(seed), tau(0.0), time_since_last_req(0.0), 
      total_missed_sales(0), messages_sent(0), messages_received(0) {}

void Customer::receive_response(int msg) {
    response_fifo.push(msg);
}

std::pair<int, int> Customer::step(double T) {
    // Process all responses in FIFO instantly
    while (!response_fifo.empty()) {
        int msg = response_fifo.front();
        response_fifo.pop();
        
        messages_received++;
        if (msg < 0) {
            total_missed_sales++;
        }
    }
    
    time_since_last_req += T;
    
    if (tau == 0.0 || time_since_last_req >= tau) {
        std::uniform_real_distribution<double> dis_tau(A, B);
        std::uniform_int_distribution<int> dis_prod(1, N);
        std::uniform_int_distribution<int> dis_server(1, S);
        
        tau = dis_tau(gen);
        time_since_last_req = 0.0;
        
        int target_server = dis_server(gen);
        int product_id = dis_prod(gen);
        messages_sent++;
        
        return {target_server, product_id};
    }
    
    return {0, 0};
}
