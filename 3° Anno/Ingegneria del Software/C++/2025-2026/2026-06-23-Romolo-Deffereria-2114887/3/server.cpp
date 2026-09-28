#include "server.hpp"
#include "network.hpp"
#include <cmath>

ServerNode::ServerNode(Engine* eng, int id, int P, int W, double tau0, double tau1, double b5)
    : Node(eng, id), P(P), W(W), tau0(tau0), tau1(tau1), sellBuy(0.0) {
    // Initialize DB
    std::uniform_int_distribution<int> dist_g(0, W);
    std::uniform_real_distribution<double> dist_v(b5, b5 * 2.0);
    for (int i = 1; i <= P; ++i) {
        db[i] = {dist_g(eng->getGen()), dist_v(eng->getGen())};
    }
}

void ServerNode::scheduleUpdate(double t) {
    std::uniform_real_distribution<double> dist_tau(tau0, tau1);
    double tau = dist_tau(engine->getGen());
    engine->schedule(t + tau, EV_SERVER_UPDATE, id);
}

void ServerNode::doUpdate(double t) {
    std::uniform_int_distribution<int> dist_p(1, P);
    int i = dist_p(engine->getGen());
    
    int g_i = db[i].g;
    int q_req = W - g_i;
    
    // Send request to supplier i
    Message m;
    m.dst_type = TYPE_SUPPLIER;
    m.dst_id = i;
    m.msg_type = MSG_SERVER_TO_SUPPLIER;
    m.i = i;
    m.q = q_req;
    
    engine->network->push(m, t);
    
    // Schedule next update
    scheduleUpdate(t);
}

void ServerNode::push(const Message& m, double t) {
    q.push(m);
    if (!busy) {
        busy = true;
        engine->schedule(t, EV_NODE_FINISH, id);
    }
}

void ServerNode::processFinish(double t) {
    if (q.empty()) {
        busy = false;
        return;
    }
    
    Message m = q.front();
    q.pop();
    
    if (m.msg_type == MSG_CUST_TO_SERVER) {
        int prod_i = m.i;
        int req_q = m.q;
        
        int g_i = db[prod_i].g;
        double v_i = db[prod_i].v;
        int k = std::min(req_q, g_i);
        
        db[prod_i].g -= k;
        sellBuy += k * v_i;
        
        // Reply to customer
        Message reply;
        reply.dst_type = TYPE_CUSTOMER;
        reply.dst_id = m.customer_id;
        reply.msg_type = MSG_SERVER_REPLY_CUST;
        reply.i = prod_i;
        reply.k = k;
        reply.v = v_i;
        
        engine->network->push(reply, t);
        
    } else if (m.msg_type == MSG_SUPPLIER_TO_SERVER) {
        int prod_i = m.i;
        int q_recv = m.q;
        double cost = m.c;
        
        db[prod_i].g += q_recv;
        sellBuy -= cost;
    }
    
    if (!q.empty()) {
        engine->schedule(t, EV_NODE_FINISH, id);
    } else {
        busy = false;
    }
}
