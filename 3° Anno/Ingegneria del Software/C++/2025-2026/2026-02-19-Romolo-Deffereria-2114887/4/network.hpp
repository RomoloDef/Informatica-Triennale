#ifndef NETWORK_HPP
#define NETWORK_HPP

#include "engine.hpp"

class NetworkNode : public Node {
private:
    double r;
    double w;

public:
    NetworkNode(Engine* eng, int id, double r, double w) : Node(eng, id), r(r), w(w) {}
    
    void push(const Message& m, double t) override {
        q.push(m);
        if (!busy) {
            busy = true;
            engine->schedule(t + r + w, EV_NODE_FINISH, id);
        }
    }
    
    void processFinish(double t) override {
        Message m = q.front();
        q.pop();
        
        // Pass to destination
        engine->route(m, t);
        
        if (!q.empty()) {
            engine->schedule(t + r + w, EV_NODE_FINISH, id);
        } else {
            busy = false;
        }
    }
};

#endif
