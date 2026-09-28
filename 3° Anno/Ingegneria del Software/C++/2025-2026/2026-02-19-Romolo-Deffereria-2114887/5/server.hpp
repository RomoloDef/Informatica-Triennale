#ifndef SERVER_HPP
#define SERVER_HPP

#include "engine.hpp"

class ServerNode : public Node {
private:
    double z;
    double v;

public:
    ServerNode(Engine* eng, int id, double z, double v) : Node(eng, id), z(z), v(v) {}
    
    void push(const Message& m, double t) override {
        q.push(m);
        if (!busy) {
            busy = true;
            engine->schedule(t + z + v, EV_NODE_FINISH, id);
        }
    }
    
    void processFinish(double t) override {
        Message m = q.front();
        q.pop();
        
        if (m.msg_type == MSG_CUST_REQ) {
            Message out;
            out.dst_type = TYPE_DB;
            out.dst_id = 0;
            out.msg_type = MSG_SERV_QUERY;
            out.s = m.s;
            out.i = m.i;
            out.c = m.c;
            out.q = m.q;
            engine->route(out, t);
        } else if (m.msg_type == MSG_DB_REPLY) {
            int k = std::min(m.q, m.g);
            engine->total_missed_sales += (m.q - k);
            engine->total_transactions += 1;
            
            Message out1;
            out1.dst_type = TYPE_DB;
            out1.dst_id = 0;
            out1.msg_type = MSG_SERV_UPDATE;
            out1.i = m.i;
            out1.k = k;
            engine->route(out1, t);
            
            // We ignore sending the reply to the customer as it doesn't affect the network or system state.
        }
        
        if (!q.empty()) {
            engine->schedule(t + z + v, EV_NODE_FINISH, id);
        } else {
            busy = false;
        }
    }
};

#endif
