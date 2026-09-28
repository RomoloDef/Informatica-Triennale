#include "ParameterizedMDP.hpp"

ParameterizedMDP::ParameterizedMDP(int num_states, double c00, double c01)
    : MDP(num_states), cost_00(c00), cost_01(c01), p(0.0) {}

void ParameterizedMDP::set_p(double new_p) {
    p = new_p;
}

double ParameterizedMDP::simulate_episode(std::mt19937& gen) const {
    int current_state = 0;
    double total_cost = 0.0;
    std::uniform_real_distribution<double> dis(0.0, 1.0);
    
    while (current_state != N - 1) {
        if (current_state == 0) {
            double roll = dis(gen);
            if (roll <= p) {
                total_cost += cost_00;
                current_state = 0;
            } else {
                total_cost += cost_01;
                current_state = 1;
            }
        } else {
            auto next = states[current_state].get_next_state_and_cost(gen);
            current_state = next.first;
            total_cost += next.second;
        }
    }
    
    return total_cost;
}
