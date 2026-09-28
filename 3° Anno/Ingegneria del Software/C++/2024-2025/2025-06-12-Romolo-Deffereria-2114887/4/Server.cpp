#include "Server.hpp"

Server::Server(int id, int N, int K, double f, std::mt19937& gen)
    : id(id), db(N + 1, 0), busy_timer(0.0), F(f) {
    std::uniform_int_distribution<int> dis_K(1, K);
    for (int i = 1; i <= N; ++i) {
        db[i] = dis_K(gen);
    }
}

void Server::push_request(int product_id) {
    fifo.push(product_id);
}

void Server::restock(int product_id, int amount) {
    db[product_id] += amount;
}

int Server::step(double T) {
    if (busy_timer > 0.0) {
        busy_timer -= T;
        return 0; // Busy
    }
    
    if (!fifo.empty()) {
        int req = fifo.front();
        fifo.pop();
        
        busy_timer = F;
        
        if (db[req] > 0) {
            db[req]--;
            return req; // Success
        } else {
            return -req; // Failure
        }
    }
    
    return 0; // Idle
}
