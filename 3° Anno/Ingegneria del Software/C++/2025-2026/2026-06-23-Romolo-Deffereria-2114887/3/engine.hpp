#ifndef ENGINE_HPP
#define ENGINE_HPP

#include "common.hpp"

enum EventType {
    EV_NODE_FINISH,
    EV_CUSTOMER_FIRE,
    EV_SERVER_UPDATE
};

struct Event {
    double time;
    EventType type;
    int node_id;
    
    bool operator<(const Event& other) const {
        return time > other.time;
    }
};

class NetworkNode;
class ServerNode;
class Customer;
class Supplier;

class Engine {
private:
    double H;
    std::mt19937 gen;
    std::priority_queue<Event> eq;

public:
    NetworkNode* network;
    ServerNode* server; // Only one server
    std::vector<Customer*> customers;
    std::vector<Supplier*> suppliers;

    Engine(double H, unsigned int seed) : H(H), gen(seed), network(nullptr), server(nullptr) {}

    void schedule(double t, EventType type, int node_id) {
        if (t <= H) {
            eq.push({t, type, node_id});
        }
    }

    bool hasEvents() const { return !eq.empty(); }
    
    Event popEvent() {
        Event e = eq.top();
        eq.pop();
        return e;
    }

    std::mt19937& getGen() { return gen; }
};

#endif
