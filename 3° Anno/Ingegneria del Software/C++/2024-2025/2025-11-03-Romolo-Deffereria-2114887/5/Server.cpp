#include "Server.hpp"

Server::Server(int P, int k_val, double v, double w, double prob, int seed)
    : db(P + 1, 0), V(v), W(w), K(k_val), p(prob), gen(seed), tau(0.0), time_since_last_proc(0.0) {
    std::uniform_int_distribution<int> dis_K(0, K);
    for (int i = 1; i <= P; ++i) {
        db[i] = dis_K(gen);
    }
}

void Server::push_customer_request(int product_id) {
    customer_fifo.push(product_id);
}

int Server::step(double T) {
    time_since_last_proc += T;
    
    if (tau == 0.0) {
        std::uniform_real_distribution<double> dis_tau(V, W);
        tau = dis_tau(gen);
    }
    
    if (time_since_last_proc >= tau) {
        if (!customer_fifo.empty()) {
            int prod = customer_fifo.front();
            customer_fifo.pop();
            
            // Set new tau for next request
            std::uniform_real_distribution<double> dis_tau(V, W);
            tau = dis_tau(gen);
            time_since_last_proc = 0.0;
            
            if (db[prod] > 0) {
                db[prod]--;
                return prod;
            } else {
                std::uniform_real_distribution<double> dis_p(0.0, 1.0);
                if (dis_p(gen) <= p) {
                    std::uniform_int_distribution<int> dis_K(0, K);
                    db[prod] = dis_K(gen);
                }
                return -prod;
            }
        }
    }
    
    return 0;
}
