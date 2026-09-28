#include "network.hpp"
#include "engine.hpp"
#include "server.hpp"
#include "customer.hpp"
#include "supplier.hpp"
#include <iostream>

void NetworkNode::push(const Message& m, double t) {
    q.push(m);
    if (!busy) {
        busy = true;
        engine->schedule(t + r, EV_NODE_FINISH, id);
    }
}

void NetworkNode::processFinish(double t) {
    if (q.empty()) {
        busy = false;
        return;
    }
    
    Message m = q.front();
    q.pop();
    
    if (m.dst_type == TYPE_SERVER) {
        if (engine->server) {
            engine->server->push(m, t);
        }
    } else if (m.dst_type == TYPE_CUSTOMER) {
        if (m.dst_id >= 1 && m.dst_id <= (int)engine->customers.size()) {
            engine->customers[m.dst_id - 1]->push(m, t);
        }
    } else if (m.dst_type == TYPE_SUPPLIER) {
        if (m.dst_id >= 1 && m.dst_id <= (int)engine->suppliers.size()) {
            engine->suppliers[m.dst_id - 1]->push(m, t);
        }
    }

    if (!q.empty()) {
        engine->schedule(t + r, EV_NODE_FINISH, id);
    } else {
        busy = false;
    }
}
