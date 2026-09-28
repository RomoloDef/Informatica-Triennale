#include "customer.hpp"
#include "network.hpp"
#include <cmath>

void Customer::fire(double t) {
    // Determine sojourn time tau
    double min_tau = a1 + b1 * product_id;
    double max_tau = a2 + b2 * product_id;
    std::uniform_real_distribution<double> dist_tau(min_tau, max_tau);
    double tau = dist_tau(engine->getGen());

    // Schedule next fire
    engine->schedule(t + tau, EV_CUSTOMER_FIRE, id);

    // Determine quantity q
    double min_q = a3 + b3 * product_id;
    double max_q = a4 + b4 * product_id;
    // According to instructions, q is integer chosen uniformly in [min_q, max_q]
    std::uniform_int_distribution<int> dist_q(std::round(min_q), std::round(max_q));
    int q_val = dist_q(engine->getGen());

    // Send request to server
    Message m;
    m.dst_type = TYPE_SERVER;
    m.dst_id = 1; // Only one server
    m.msg_type = MSG_CUST_TO_SERVER;
    m.i = product_id;
    m.q = q_val;
    m.customer_id = product_id; // id for routing replies
    
    engine->network->push(m, t);
}

void Customer::push(const Message& m, double t) {
    q.push(m);
    if (!busy) {
        busy = true;
        engine->schedule(t, EV_NODE_FINISH, id);
    }
}

void Customer::processFinish(double t) {
    if (q.empty()) {
        busy = false;
        return;
    }
    
    // We pop the message, the customer receives the reply (k, v) but doesn't need to do anything with it
    q.pop();
    
    if (!q.empty()) {
        engine->schedule(t, EV_NODE_FINISH, id);
    } else {
        busy = false;
    }
}
