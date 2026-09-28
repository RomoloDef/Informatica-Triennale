#include "customer.hpp"
#include <algorithm>

Customer::Customer() : id(0), state(0), V(0), 
    tau_low(0), tau_high(0),
    cycle_start_time(0), total_cycle_time(0), completed_cycles(0) {}

void Customer::init(int customer_id, int v, int P,
                    double a1, double b1, double a2, double b2,
                    std::mt19937& gen) {
    id = customer_id;
    V = v;
    state = 0;
    cycle_start_time = 0.0;
    total_cycle_time = 0.0;
    completed_cycles = 0;
    
    int i = customer_id;
    tau_low = a1 + b1 * i;
    tau_high = a2 + b2 * i;
    
    std::vector<int> all_products(P);
    for (int p = 0; p < P; ++p) {
        all_products[p] = p + 1;
    }
    std::shuffle(all_products.begin(), all_products.end(), gen);
    products.resize(V);
    for (int j = 0; j < V; ++j) {
        products[j] = all_products[j];
    }
}

double Customer::getTau(std::mt19937& gen) const {
    std::uniform_real_distribution<double> dist(tau_low, tau_high);
    return dist(gen);
}

void Customer::transitionToNextState() {
    if (state < V) {
        state++;
    } else {
        state = 0; 
    }
}

void Customer::startNewCycle(double t) {
    cycle_start_time = t;
    state = 0;
}

void Customer::completeCycle(double t) {
    double cycle_time = t - cycle_start_time;
    total_cycle_time += cycle_time;
    completed_cycles++;
}

double Customer::getAverageCycleTime() const {
    if (completed_cycles == 0) return 0.0;
    return total_cycle_time / completed_cycles;
}
