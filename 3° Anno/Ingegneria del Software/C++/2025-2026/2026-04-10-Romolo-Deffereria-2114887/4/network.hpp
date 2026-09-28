#ifndef NETWORK_HPP
#define NETWORK_HPP

#include "engine.hpp"

class NetworkNode : public Node {
private:
    double r; // message transmission delay

public:
    NetworkNode(Engine* eng, int id, double r) : Node(eng, id), r(r) {}

    void push(const Message& m, double t) override {
        q.push(m);
        if (!busy) {
            busy = true;
            engine->schedule(t + r, EV_NODE_FINISH, id);
        }
    }

    void processFinish(double t) override {
        Message m = q.front();
        q.pop();

        // Route message to actual destination
        engine->route(m, t);

        if (!q.empty()) {
            engine->schedule(t + r, EV_NODE_FINISH, id);
        } else {
            busy = false;
        }
    }
};

#endif
