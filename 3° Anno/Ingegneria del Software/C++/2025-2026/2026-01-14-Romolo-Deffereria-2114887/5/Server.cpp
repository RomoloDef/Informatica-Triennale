#include "Server.hpp"
#include "Network.hpp"
#include <random>

extern std::mt19937 gen;

Server::Server(int id, Network* net, int P, int Q) : id(id), net(net) {
    db.resize(P + 1);
    std::uniform_int_distribution<int> dist(0, Q);
    for (int i = 1; i <= P; ++i) {
        db[i] = dist(gen);
    }
}

void Server::receive_msg(const Msg& m) {
    fifo.push(m);
}

void Server::update() {
    while (!fifo.empty()) {
        Msg m = fifo.front();
        fifo.pop();
        if (m.type == 0) {
            int avail = db[m.product_i];
            int k = (avail >= m.quantity_q) ? m.quantity_q : avail;
            db[m.product_i] -= k;
            if (k < m.quantity_q) {
                net->log_missed_sale();
            }
        } else {
            db[m.product_i] += m.quantity_q;
        }
    }
}
