#ifndef DB_HPP
#define DB_HPP

#include "engine.hpp"
#include <map>

class DBNode : public Node {
private:
    double l;
    double s;
    std::map<int, int> items; // product_id -> quantity

public:
    DBNode(Engine* eng, int id, double l, double s, int P, int Q) : Node(eng, id), l(l), s(s) {
        std::uniform_int_distribution<int> dist(0, Q);
        for (int i = 1; i <= P; ++i) {
            items[i] = dist(eng->getGen());
        }
    }
    
    void push(const Message& m, double t) override {
        q.push(m);
        if (!busy) {
            busy = true;
            double delay = 0;
            if (m.msg_type == MSG_SERV_QUERY) delay = l + s;
            else if (m.msg_type == MSG_SERV_UPDATE) delay = l;
            else if (m.msg_type == MSG_SUPP_RESTOCK) delay = l;
            engine->schedule(t + delay, EV_NODE_FINISH, id);
        }
    }
    
    void processFinish(double t) override {
        Message m = q.front();
        q.pop();
        
        if (m.msg_type == MSG_SERV_QUERY) {
            int g = items[m.i];
            Message out;
            out.dst_type = TYPE_SERVER;
            out.dst_id = m.s;
            out.msg_type = MSG_DB_REPLY;
            out.s = m.s;
            out.i = m.i;
            out.c = m.c;
            out.q = m.q;
            out.g = g;
            engine->route(out, t);
        } else if (m.msg_type == MSG_SERV_UPDATE) {
            items[m.i] = std::max(0, items[m.i] - m.k);
        } else if (m.msg_type == MSG_SUPP_RESTOCK) {
            items[m.i] += m.q;
        }
        
        if (!q.empty()) {
            Message next_m = q.front();
            double delay = 0;
            if (next_m.msg_type == MSG_SERV_QUERY) delay = l + s;
            else if (next_m.msg_type == MSG_SERV_UPDATE) delay = l;
            else if (next_m.msg_type == MSG_SUPP_RESTOCK) delay = l;
            engine->schedule(t + delay, EV_NODE_FINISH, id);
        } else {
            busy = false;
        }
    }
};

#endif
