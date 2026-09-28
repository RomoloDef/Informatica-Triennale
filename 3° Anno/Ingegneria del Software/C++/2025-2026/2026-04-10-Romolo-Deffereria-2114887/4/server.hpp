#ifndef SERVER_HPP
#define SERVER_HPP

#include "engine.hpp"
#include <map>
#include <vector>
#include <cmath>

class ServerNode : public Node {
private:
    int server_index;   // 1-based index of this server
    int P;              // number of products
    int Q;              // max quantity parameter
    double tauS;        // update interval (ST0 or ST1)
    double SEP_or_SOP;  // probability for even [odd] product selection
    double QEA_or_QOA;  // probability for even [odd] quantity selection

    double sellBuy;     // reward variable
    double y;           // storage cost variable

    // Cache: product_id -> (quantity, unit_cost)
    std::map<int, std::pair<int, double>> cache;

    // Helper: select from even or odd indices
    int selectWithParity(double prob_even_or_matching, int max_val, bool server_is_even) {
        std::vector<int> matching, non_matching;
        for (int idx = 1; idx <= max_val; ++idx) {
            bool idx_even = (idx % 2 == 0);
            if (server_is_even) {
                if (idx_even) matching.push_back(idx);
                else non_matching.push_back(idx);
            } else {
                if (!idx_even) matching.push_back(idx);
                else non_matching.push_back(idx);
            }
        }

        if (matching.empty()) {
            std::uniform_int_distribution<int> dist(0, non_matching.size() - 1);
            return non_matching[dist(engine->getGen())];
        }
        if (non_matching.empty()) {
            std::uniform_int_distribution<int> dist(0, matching.size() - 1);
            return matching[dist(engine->getGen())];
        }

        std::uniform_real_distribution<double> dist01(0.0, 1.0);
        double r = dist01(engine->getGen());
        if (r < prob_even_or_matching) {
            std::uniform_int_distribution<int> dist(0, matching.size() - 1);
            return matching[dist(engine->getGen())];
        } else {
            std::uniform_int_distribution<int> dist(0, non_matching.size() - 1);
            return non_matching[dist(engine->getGen())];
        }
    }

public:
    ServerNode(Engine* eng, int node_id, int server_index, int P, int Q,
               double tauS, double SEP_or_SOP, double QEA_or_QOA)
        : Node(eng, node_id), server_index(server_index), P(P), Q(Q),
          tauS(tauS), SEP_or_SOP(SEP_or_SOP), QEA_or_QOA(QEA_or_QOA),
          sellBuy(0.0), y(0.0) {
        // Initialize cache: all products with 0 quantity, 0 cost
        for (int i = 1; i <= P; ++i) {
            cache[i] = {0, 0.0};
        }
    }

    double getSellBuy() const { return sellBuy; }
    double getY() const { return y; }

    // Update storage costs: y(s, t+T) = y(s,t) + T^0.1 * sum(alpha(s,i))
    void updateStorageCost(double T_interval) {
        double sum_alpha = 0.0;
        for (int i = 1; i <= P; ++i) {
            if (cache.count(i)) {
                auto& [q_val, v_val] = cache[i];
                sum_alpha += q_val * v_val; // alpha(s,i) = q*v
            }
        }
        y += std::pow(T_interval, 0.1) * sum_alpha;
    }

    // Schedule periodic cache update
    void scheduleUpdate(double t) {
        engine->schedule(t + tauS, EV_SERVER_UPDATE, id);
    }

    // Called when it's time to update cache from DB
    void doUpdate(double t) {
        bool is_even = (server_index % 2 == 0);
        int i = selectWithParity(SEP_or_SOP, P, is_even);
        int q = selectWithParity(QEA_or_QOA, Q, is_even);

        // Send request to DB through network
        Message out;
        out.dst_type = TYPE_DB;
        out.dst_id = 0;
        out.msg_type = MSG_SERVER_TO_DB;
        out.s = server_index;
        out.i = i;
        out.q = q;

        engine->network->push(out, t);

        // Update storage cost
        updateStorageCost(tauS);

        // Schedule next update
        scheduleUpdate(t);
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

        if (m.msg_type == MSG_CUST_TO_SERVER) {
            // Customer requests (i, q) from this server
            // Check local cache
            int prod = m.i;
            int requested = m.q;
            int available = 0;
            double cost = 0.0;
            if (cache.count(prod)) {
                available = cache[prod].first;
                cost = cache[prod].second;
            }
            int k = std::min(requested, available);

            // Decrement cache
            if (cache.count(prod)) {
                cache[prod].first -= k;
            }

            // Increment SellBuy by k*v
            sellBuy += k * cost;

            // Reply to customer (i, k, v) - through network
            // (Customer doesn't need reply for simulation, but we send it)
            Message reply;
            reply.dst_type = TYPE_CUSTOMER;
            reply.dst_id = m.c;
            reply.msg_type = MSG_SERVER_REPLY_CUST;
            reply.i = prod;
            reply.k = k;
            reply.v = cost;
            reply.c = m.c;
            // We route through network but customer doesn't process it
            // Actually the customer "waits" for reply but it doesn't affect simulation
            // Just send via network
            engine->network->push(reply, t);

        } else if (m.msg_type == MSG_DB_REPLY_SERVER) {
            // DB replied with (i, k, v) - server got items from DB
            int prod = m.i;
            int k = m.k;
            double v = m.v;

            // Increment cache quantity
            if (cache.count(prod)) {
                cache[prod].first += k;
                cache[prod].second = v; // update cost
            } else {
                cache[prod] = {k, v};
            }

            // Decrement SellBuy by k*v (paid for items)
            sellBuy -= k * v;
        }

        if (!q.empty()) {
            engine->schedule(t, EV_NODE_FINISH, id);
        } else {
            busy = false;
        }
    }
};

#endif
