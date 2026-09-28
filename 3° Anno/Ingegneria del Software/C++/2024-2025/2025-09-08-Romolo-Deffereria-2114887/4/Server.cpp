#include "Server.hpp"

Server::Server(int id, int P, int K, std::mt19937& gen)
    : id(id), db(P + 1, 0) {
    std::uniform_int_distribution<int> dis_K(0, K);
    for (int i = 1; i <= P; ++i) {
        db[i] = dis_K(gen);
    }
}

void Server::push_customer_request(int customer_id, int product_id) {
    customer_fifo.push({customer_id, product_id});
}

void Server::push_provider_restock(int product_id) {
    provider_fifo.push(product_id);
}

std::vector<std::pair<int, int>> Server::step() {
    // Process all provider restocks first
    while (!provider_fifo.empty()) {
        int prod = provider_fifo.front();
        provider_fifo.pop();
        db[prod]++;
    }
    
    // Process all customer requests
    std::vector<std::pair<int, int>> responses;
    while (!customer_fifo.empty()) {
        auto req = customer_fifo.front();
        customer_fifo.pop();
        
        int prod = req.product_id;
        if (db[prod] > 0) {
            db[prod]--;
            responses.push_back({req.customer_id, prod});
        } else {
            responses.push_back({req.customer_id, -prod});
        }
    }
    
    return responses;
}
