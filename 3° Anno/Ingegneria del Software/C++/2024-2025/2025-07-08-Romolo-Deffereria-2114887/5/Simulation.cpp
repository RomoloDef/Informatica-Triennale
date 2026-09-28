#include "Simulation.hpp"

Simulation::Simulation(double h, double t, int n, double a, double b, double prob, int s, double f, double g, int k, int q_amount, int random_seed)
    : H(h), T(t), N(n), A(a), B(b), p(prob), S(s), F(f), G(g), K(k), Q(q_amount), seed(random_seed) {}

std::pair<long long, double> Simulation::run() {
    std::mt19937 gen(seed);
    
    Customer customer(N, S, A, B, seed + 1);
    
    std::vector<std::unique_ptr<Server>> servers;
    servers.push_back(nullptr); // Index 0 unused
    for (int i = 1; i <= S; ++i) {
        servers.push_back(std::make_unique<Server>(i, N, K, F, G, p, Q, gen));
    }
    
    double current_time = 0.0;
    while (current_time <= H + 1e-9) {
        auto req_pair = customer.step(current_time == 0.0 ? 0.0 : T);
        int target_server = req_pair.first;
        int req_prod = req_pair.second;
        
        if (req_prod > 0) {
            servers[target_server]->push_request(req_prod);
        }
        
        for (int i = 1; i <= S; ++i) {
            int result = servers[i]->step(T, gen);
            if (result != 0) {
                customer.receive_response(result);
            }
        }
        
        current_time += T;
    }
    
    long long total_missed = customer.get_missed_sales();
    long long sent = customer.get_messages_sent();
    long long received = customer.get_messages_received();
    double W = 0.0;
    if (sent > 0) {
        W = (double)received / sent;
    }
    
    return {total_missed, W};
}
