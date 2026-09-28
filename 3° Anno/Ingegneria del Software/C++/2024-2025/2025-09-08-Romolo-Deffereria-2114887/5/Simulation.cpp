#include "Simulation.hpp"

Simulation::Simulation(double t, double h, int c, double a, double b, int f_prov, double v, double q, int p, int s, int k, int random_seed)
    : T(t), H(h), C(c), A(a), B(b), F_prov(f_prov), V(v), Q(q), P(p), S(s), K(k), seed(random_seed) {}

long long Simulation::run_and_get_missed_sales() {
    std::mt19937 gen(seed);
    
    std::vector<std::unique_ptr<Customer>> customers;
    for (int i = 0; i < C; ++i) {
        customers.push_back(std::make_unique<Customer>(A, B, S, P, gen()));
    }
    
    std::vector<std::unique_ptr<Provider>> providers;
    for (int i = 0; i < F_prov; ++i) {
        providers.push_back(std::make_unique<Provider>(V, Q, S, P, gen()));
    }
    
    std::vector<std::unique_ptr<Server>> servers;
    servers.push_back(nullptr); // Index 0 unused
    for (int i = 1; i <= S; ++i) {
        servers.push_back(std::make_unique<Server>(i, P, K, gen));
    }
    
    double current_time = 0.0;
    while (current_time <= H + 1e-9) {
        if (current_time > 0.0) {
            for (int i = 0; i < C; ++i) {
                auto req = customers[i]->step(T);
                if (req.first != 0) {
                    servers[req.first]->push_customer_request(i, req.second);
                }
            }
            
            for (int i = 0; i < F_prov; ++i) {
                auto req = providers[i]->step(T);
                if (req.first != 0) {
                    servers[req.first]->push_provider_restock(req.second);
                }
            }
        }
        
        for (int i = 1; i <= S; ++i) {
            auto responses = servers[i]->step();
            for (auto& resp : responses) {
                customers[resp.first]->receive_response(resp.second);
            }
        }
        
        current_time += T;
    }
    
    long long total_missed = 0;
    for (int i = 0; i < C; ++i) {
        total_missed += customers[i]->get_missed_sales();
    }
    
    return total_missed;
}
