#include "Dispatcher.hpp"

Dispatcher::Dispatcher(double d, double prob, int s, int n, int seed)
    : busy_timer(0.0), D(d), p(prob), S(s), N(n), gen(seed), alpha_missed(0), beta_requests(0) {}

void Dispatcher::push_customer_request(int product_id) {
    customer_fifo.push(product_id);
}

void Dispatcher::push_server_message(int server_id, int product_id, int status) {
    server_fifo.push({server_id, product_id, status});
}

void Dispatcher::step(double T, std::vector<std::unique_ptr<Server>>& servers) {
    // Process server messages instantly
    while (!server_fifo.empty()) {
        ServerMessage msg = server_fifo.front();
        server_fifo.pop();
        
        if (msg.status == 0) {
            alpha_missed++;
            
            std::uniform_real_distribution<double> dis_p(0.0, 1.0);
            if (dis_p(gen) < p) {
                servers[msg.server_id]->restock(msg.product_id, 10);
            } else {
                std::uniform_int_distribution<int> dis_s(1, S);
                std::uniform_int_distribution<int> dis_n(1, N);
                servers[dis_s(gen)]->restock(dis_n(gen), 10);
            }
        }
    }
    
    // Process customer requests
    if (busy_timer > 0.0) {
        busy_timer -= T;
    } else {
        if (!customer_fifo.empty()) {
            int req = customer_fifo.front();
            customer_fifo.pop();
            
            std::uniform_int_distribution<int> dis_s(1, S);
            int target_server = dis_s(gen);
            
            servers[target_server]->push_request(req);
            beta_requests++;
            
            busy_timer = D;
        }
    }
}
