#include "Provider.hpp"

Provider::Provider(double v, double q, int s, int p, int seed)
    : V(v), Q(q), S(s), P(p), gen(seed), gamma(0.0), time_since_last_restock(0.0) {}

std::pair<int, int> Provider::step(double T) {
    time_since_last_restock += T;
    
    if (gamma == 0.0 || time_since_last_restock >= gamma) {
        std::uniform_real_distribution<double> dis_gamma(V, Q);
        std::uniform_int_distribution<int> dis_server(1, S);
        std::uniform_int_distribution<int> dis_prod(1, P);
        
        gamma = dis_gamma(gen);
        time_since_last_restock = 0.0;
        
        return {dis_server(gen), dis_prod(gen)};
    }
    
    return {0, 0};
}
