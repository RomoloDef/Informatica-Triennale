#ifndef DB_HPP
#define DB_HPP

#include "engine.hpp"
#include <map>

class DBNode : public Node {
private:
    int P;
    // product_id -> (quantity, unit_cost)
    std::map<int, std::pair<int, double>> products;

public:
    DBNode(Engine* eng, int id, int P, int Q) : Node(eng, id), P(P) {
        // Initialize: for each product, random quantity in [0, Q] and random cost in [1, 100]
        std::uniform_int_distribution<int> dist_q(0, Q);
        std::uniform_int_distribution<int> dist_v(1, 100);
        for (int i = 1; i <= P; ++i) {
            int qty = dist_q(eng->getGen());
            int cost = dist_v(eng->getGen());
            products[i] = {qty, static_cast<double>(cost)};
        }
    }

    void push(const Message& m, double t) override {
        q.push(m);
        if (!busy) {
            busy = true;
            engine->schedule(t, EV_NODE_FINISH, id);
        }
    }

    void processFinish(double t) override {
        if (q.empty()) {
            busy = false;
            return;
        }

        Message m = q.front();
        q.pop();

        if (m.msg_type == MSG_SUPPLIER_TO_DB) {
            // Supplier sends (i, q): increment quantity of product i by q
            int prod = m.i;
            if (products.count(prod)) {
                products[prod].first += m.q;
            }

            // Send ack to supplier through network
            Message ack;
            ack.dst_type = TYPE_SUPPLIER;
            ack.dst_id = 0;
            ack.msg_type = MSG_DB_ACK_SUPPLIER;
            // Route through network (supplier doesn't process it, just for completeness)
            engine->network->push(ack, t);

        } else if (m.msg_type == MSG_SERVER_TO_DB) {
            // Server requests (i, q)
            int prod = m.i;
            int requested = m.q;
            int available = 0;
            double cost = 0.0;
            if (products.count(prod)) {
                available = products[prod].first;
                cost = products[prod].second;
            }
            int k = std::min(requested, available);

            // Decrement DB quantity
            if (products.count(prod)) {
                products[prod].first -= k;
            }

            // Reply to server with (i, k, v)
            Message reply;
            reply.dst_type = TYPE_SERVER;
            reply.dst_id = m.s;
            reply.msg_type = MSG_DB_REPLY_SERVER;
            reply.i = prod;
            reply.k = k;
            reply.v = cost;
            reply.s = m.s;

            engine->network->push(reply, t);
        }

        if (!q.empty()) {
            engine->schedule(t, EV_NODE_FINISH, id);
        } else {
            busy = false;
        }
    }
};

#endif
