#include "Server.hpp"

Server::Server(int id, int N, int K, double f, double g, double p_restock, int q_amount, std::mt19937& gen)
    : id(id), db(N + 1, 0), busy_timer(0.0), F(f), G(g), p(p_restock), Q(q_amount) {
    std::uniform_int_distribution<int> dis_K(0, K);
    for (int i = 1; i <= N; ++i) {
        db[i] = dis_K(gen);
    }
}

void Server::push_request(int product_id) {
    fifo.push(product_id);
}

int Server::step(double T, std::mt19937& gen) {
    if (busy_timer > 0.0) {
        busy_timer -= T;
        return 0; // Busy
    }
    
    if (!fifo.empty()) {
        int req = fifo.front();
        fifo.pop();
        
        if (db[req] > 0) {
            db[req]--;
            busy_timer = F;
            return req; // Success
        } else {
            std::uniform_real_distribution<double> dis_p(0.0, 1.0);
            if (dis_p(gen) < p) {
                db[req] += Q;
                busy_timer = G;
            } else {
                busy_timer = F;
            }
            return -req; // Failure (mancata vendita)
        }
    }
    
    return 0; // Idle
}
