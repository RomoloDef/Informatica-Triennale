#include "network.hpp"
#include <queue>
#include <algorithm>
#include <cmath>
#include <functional>


enum EventType {
    EV_CUSTOMER_WAIT_DONE,    
    EV_SERVER_RESPONSE,       
    EV_CUSTOMER_TIMEOUT       
};

struct Event {
    double time;
    EventType type;
    int customer_id;  
    int server_id;    
    int product;
    int request_seq;  

    bool operator>(const Event& other) const {
        return time > other.time;
    }
};

Network::Network() : P(0), K(0), C(0), V(0), r(0) {}

void Network::init(int p, int k, int c, int v, double r_val,
                   double a1, double b1, double a2, double b2,
                   double a3, double b3, double a4, double b4,
                   double a5, double b5, double a6, double b6,
                   double a7, double b7,
                   std::mt19937& gen) {
    P = p; K = k; C = c; V = v; r = r_val;

    
    servers.resize(K * P);
    for (int s = 0; s < K * P; ++s) {
        servers[s].init(s + 1, P, a2, b2, a3, b3, a4, b4, a5, b5, a6, b6, a7, b7, gen);
    }

    
    customers.resize(C);
    for (int i = 0; i < C; ++i) {
        customers[i].init(i + 1, V, P, a1, b1, a2, b2, gen);
    }
}

std::vector<int> Network::getServersForProduct(int p) const {
    std::vector<int> result;
    for (int s = 0; s < K * P; ++s) {
        if (servers[s].getProduct() == p) {
            result.push_back(s);
        }
    }
    return result;
}


static void schedulePurchaseRequest(
    std::priority_queue<Event, std::vector<Event>, std::greater<Event>>& pq,
    int ci, int product, double time, int req_seq, double H)
{
    Event ev;
    ev.time = time;
    ev.type = EV_CUSTOMER_WAIT_DONE;  
    ev.customer_id = ci;
    ev.server_id = -1;
    ev.product = product;
    ev.request_seq = req_seq;
    if (ev.time <= H) pq.push(ev);
}

void Network::simulate(double H, std::mt19937& gen, double& R_H, std::vector<double>& Q) {
    std::priority_queue<Event, std::vector<Event>, std::greater<Event>> pq;

    
    std::vector<int> customer_req_seq(C, 0);

    
    for (int i = 0; i < C; ++i) {
        customers[i].startNewCycle(0.0);
        double tau = customers[i].getTau(gen);
        
        int product_to_buy = customers[i].getProductAt(1);
        schedulePurchaseRequest(pq, i, product_to_buy, tau, customer_req_seq[i], H);
    }

    while (!pq.empty()) {
        Event ev = pq.top();
        pq.pop();

        if (ev.time > H) break;

        if (ev.type == EV_CUSTOMER_WAIT_DONE) {
            
            if (ev.request_seq != customer_req_seq[ev.customer_id]) continue;

            int ci = ev.customer_id;
            Customer& cust = customers[ci];

            
            cust.transitionToNextState();
            int product_to_buy = ev.product;

            
            std::vector<int> eligible_servers = getServersForProduct(product_to_buy);
            if (eligible_servers.empty()) continue; 

            std::uniform_int_distribution<int> dist_srv(0, eligible_servers.size() - 1);
            int srv_idx = eligible_servers[dist_srv(gen)];

            
            servers[srv_idx].updateState(ev.time, gen);

            if (servers[srv_idx].isWorkingAt(ev.time)) {
                
                double B = servers[srv_idx].getServiceTime(gen);
                double response_time = ev.time + r + B + r;

                Event resp_ev;
                resp_ev.time = response_time;
                resp_ev.type = EV_SERVER_RESPONSE;
                resp_ev.customer_id = ci;
                resp_ev.server_id = srv_idx;
                resp_ev.product = product_to_buy;
                resp_ev.request_seq = customer_req_seq[ci];
                if (resp_ev.time <= H) pq.push(resp_ev);

                
                double z = servers[srv_idx].getServiceTime(gen);
                double timeout_val = 3.0 * z;
                Event to_ev;
                to_ev.time = ev.time + timeout_val;
                to_ev.type = EV_CUSTOMER_TIMEOUT;
                to_ev.customer_id = ci;
                to_ev.server_id = srv_idx;
                to_ev.product = product_to_buy;
                to_ev.request_seq = customer_req_seq[ci];
                if (to_ev.time <= H) pq.push(to_ev);
            } else {
                
                double z = servers[srv_idx].getServiceTime(gen);
                double timeout_val = 3.0 * z;
                Event to_ev;
                to_ev.time = ev.time + timeout_val;
                to_ev.type = EV_CUSTOMER_TIMEOUT;
                to_ev.customer_id = ci;
                to_ev.server_id = srv_idx;
                to_ev.product = product_to_buy;
                to_ev.request_seq = customer_req_seq[ci];
                if (to_ev.time <= H) pq.push(to_ev);
            }

        } else if (ev.type == EV_SERVER_RESPONSE) {
            if (ev.request_seq != customer_req_seq[ev.customer_id]) continue;

            int ci = ev.customer_id;
            Customer& cust = customers[ci];

            
            customer_req_seq[ci]++;

            
            if (cust.getState() >= cust.getV()) {
                
                cust.completeCycle(ev.time);
                cust.startNewCycle(ev.time);
                

                double tau = cust.getTau(gen);
                int next_product = cust.getProductAt(1);
                schedulePurchaseRequest(pq, ci, next_product, ev.time + tau, customer_req_seq[ci], H);
            } else {

                double tau = cust.getTau(gen);
                int next_state = cust.getState() + 1;
                int next_product = cust.getProductAt(next_state);
                schedulePurchaseRequest(pq, ci, next_product, ev.time + tau, customer_req_seq[ci], H);
            }

        } else if (ev.type == EV_CUSTOMER_TIMEOUT) {
            if (ev.request_seq != customer_req_seq[ev.customer_id]) continue;

            int ci = ev.customer_id;
            Customer& cust = customers[ci];


            customer_req_seq[ci]++;

            int product_to_buy = ev.product;
            std::vector<int> eligible_servers = getServersForProduct(product_to_buy);
            std::uniform_int_distribution<int> dist_srv(0, eligible_servers.size() - 1);
            int srv_idx = eligible_servers[dist_srv(gen)];

            servers[srv_idx].updateState(ev.time, gen);

            if (servers[srv_idx].isWorkingAt(ev.time)) {
                double B = servers[srv_idx].getServiceTime(gen);
                double response_time = ev.time + r + B + r;

                Event resp_ev;
                resp_ev.time = response_time;
                resp_ev.type = EV_SERVER_RESPONSE;
                resp_ev.customer_id = ci;
                resp_ev.server_id = srv_idx;
                resp_ev.product = product_to_buy;
                resp_ev.request_seq = customer_req_seq[ci];
                if (resp_ev.time <= H) pq.push(resp_ev);

                double z = servers[srv_idx].getServiceTime(gen);
                double timeout_val = 3.0 * z;
                Event to_ev;
                to_ev.time = ev.time + timeout_val;
                to_ev.type = EV_CUSTOMER_TIMEOUT;
                to_ev.customer_id = ci;
                to_ev.server_id = srv_idx;
                to_ev.product = product_to_buy;
                to_ev.request_seq = customer_req_seq[ci];
                if (to_ev.time <= H) pq.push(to_ev);
            } else {
                double z = servers[srv_idx].getServiceTime(gen);
                double timeout_val = 3.0 * z;
                Event to_ev;
                to_ev.time = ev.time + timeout_val;
                to_ev.type = EV_CUSTOMER_TIMEOUT;
                to_ev.customer_id = ci;
                to_ev.server_id = srv_idx;
                to_ev.product = product_to_buy;
                to_ev.request_seq = customer_req_seq[ci];
                if (to_ev.time <= H) pq.push(to_ev);
            }
        }
    }


    Q.resize(C);
    double sum_Q = 0.0;
    for (int i = 0; i < C; ++i) {
        Q[i] = customers[i].getAverageCycleTime();
        sum_Q += Q[i];
    }
    R_H = sum_Q / C;
}
