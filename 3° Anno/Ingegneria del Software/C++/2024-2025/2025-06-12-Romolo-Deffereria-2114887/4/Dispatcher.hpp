#ifndef DISPATCHER_HPP
#define DISPATCHER_HPP

#include "Server.hpp"
#include <queue>
#include <vector>
#include <memory>

struct ServerMessage {
    int server_id;
    int product_id;
    int status; // 1 for success, 0 for failure
};

class Dispatcher {
private:
    std::queue<int> customer_fifo;
    std::queue<ServerMessage> server_fifo;
    
    double busy_timer;
    double D;
    double p;
    int S;
    int N;
    std::mt19937 gen;
    
    long long alpha_missed;
    long long beta_requests;

public:
    Dispatcher(double D, double p, int S, int N, int seed);
    
    void push_customer_request(int product_id);
    void push_server_message(int server_id, int product_id, int status);
    
    void step(double T, std::vector<std::unique_ptr<Server>>& servers);
    
    long long get_alpha() const { return alpha_missed; }
    long long get_beta() const { return beta_requests; }
};

#endif // DISPATCHER_HPP
