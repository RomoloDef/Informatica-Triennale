#include "supplier.hpp"
#include "network.hpp"

void Supplier::push(const Message& m, double t) {
    q.push(m);
    if (!busy) {
        busy = true;
        engine->schedule(t, EV_NODE_FINISH, id);
    }
}

void Supplier::processFinish(double t) {
    if (q.empty()) {
        busy = false;
        return;
    }
    
    Message m = q.front();
    q.pop();
    
    if (m.msg_type == MSG_SERVER_TO_SUPPLIER) {
        int q_req = m.q;
        double cost = a5 + b5 * q_req;
        
        Message reply;
        reply.dst_type = TYPE_SERVER;
        reply.dst_id = 1;
        reply.msg_type = MSG_SUPPLIER_TO_SERVER;
        reply.i = m.i;
        reply.q = q_req;
        reply.c = cost;
        
        engine->network->push(reply, t);
    }
    
    if (!q.empty()) {
        engine->schedule(t, EV_NODE_FINISH, id);
    } else {
        busy = false;
    }
}
