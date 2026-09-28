#include "Simulation.hpp"

Simulation::Simulation(double t, double h, double a, double b, double v, double w, int p_val, int k_val, double prob, int random_seed)
    : T(t), H(h), A(a), B(b), V(v), W(w), P(p_val), K(k_val), p(prob), seed(random_seed) {}

long long Simulation::run_and_get_missed_sales() {
    std::mt19937 gen(seed);
    
    Customer customer(A, B, P, gen());
    Server server(P, K, V, W, p, gen());
    
    double current_time = 0.0;
    while (current_time <= H + 1e-9) {
        if (current_time > 0.0) {
            int req = customer.step(T);
            if (req != 0) {
                server.push_customer_request(req);
            }
        }
        
        int resp = server.step(T);
        if (resp != 0) {
            customer.receive_response(resp);
        }
        
        current_time += T;
    }
    
    return customer.get_missed_sales();
}
