#ifndef ENGINE_HPP
#define ENGINE_HPP

#include "common.hpp"
#include <queue>
#include <random>

enum EventType {
    EV_NODE_FINISH,
    EV_CUSTOMER_FIRE,
    EV_SUPPLIER_FIRE
};

struct Event {
    double time;
    EventType type;
    int node_id; // For CUSTOMER_FIRE/SUPPLIER_FIRE, this is customer/supplier ID. For NODE_FINISH, this is node ID.
    
    bool operator>(const Event& other) const {
        return time > other.time;
    }
};

class Engine {
private:
    std::priority_queue<Event, std::vector<Event>, std::greater<Event> > pq;
    double H;
    std::mt19937 gen;

public:
    int total_missed_sales = 0;
    int total_transactions = 0;
    
    Node* network = nullptr;
    std::vector<Node*> servers;
    Node* db = nullptr;
    
    Engine(double H, int seed) : H(H), gen(seed) {}
    
    void schedule(double time, EventType type, int node_id) {
        if (time <= H) {
            Event ev; ev.time = time; ev.type = type; ev.node_id = node_id;
            pq.push(ev);
        }
    }
    
    std::mt19937& getGen() { return gen; }
    
    bool hasEvents() const { return !pq.empty(); }
    Event popEvent() {
        Event e = pq.top();
        pq.pop();
        return e;
    }
    
    void route(const Message& m, double t) {
        if (m.dst_type == TYPE_NETWORK) {
            network->push(m, t);
        } else if (m.dst_type == TYPE_SERVER) {
            if (m.dst_id >= 1 && m.dst_id <= (int)servers.size()) {
                servers[m.dst_id - 1]->push(m, t);
            }
        } else if (m.dst_type == TYPE_DB) {
            db->push(m, t);
        }
    }
};

#endif
