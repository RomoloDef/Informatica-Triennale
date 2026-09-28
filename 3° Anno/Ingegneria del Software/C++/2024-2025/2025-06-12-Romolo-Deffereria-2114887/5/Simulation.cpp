#include "Simulation.hpp"

Simulation::Simulation(double h, int n, double a, double b, double t, int s, int k, double prob, double d, double f, int random_seed)
    : H(h), N(n), A(a), B(b), T(t), S(s), K(k), p(prob), D(d), F(f), seed(random_seed) {}

std::pair<long long, long long> Simulation::run() {
    std::mt19937 gen(seed);
    
    Customer customer(N, A, B, seed + 1);
    Dispatcher dispatcher(D, p, S, N, seed + 2);
    
    std::vector<std::unique_ptr<Server>> servers;
    servers.push_back(nullptr); // Index 0 unused
    for (int i = 1; i <= S; ++i) {
        servers.push_back(std::make_unique<Server>(i, N, K, F, gen));
    }
    
    double current_time = 0.0;
    while (current_time <= H + 1e-9) {
        int req = customer.step(current_time == 0.0 ? 0.0 : T);
        if (req > 0) {
            dispatcher.push_customer_request(req);
        }
        
        dispatcher.step(T, servers);
        
        for (int i = 1; i <= S; ++i) {
            int result = servers[i]->step(T);
            if (result > 0) {
                dispatcher.push_server_message(i, result, 1);
            } else if (result < 0) {
                dispatcher.push_server_message(i, -result, 0);
            }
        }
        
        current_time += T;
    }
    
    return {dispatcher.get_alpha(), dispatcher.get_beta()};
}
