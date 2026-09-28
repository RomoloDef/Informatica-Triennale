#include "MDP.hpp"

State::State(int id) : id(id) {}

void State::add_transition(int target, double prob, double cost) {
    transitions.push_back({target, prob, cost});
}

std::pair<int, double> State::get_next_state_and_cost(std::mt19937& gen) const {
    std::uniform_real_distribution<double> dis(0.0, 1.0);
    double p = dis(gen);
    double cumulative = 0.0;
    
    for (const auto& t : transitions) {
        cumulative += t.probability;
        if (p <= cumulative) {
            return {t.target_state, t.cost};
        }
    }
    
    // Fallback if probabilities don't sum to exactly 1.0 due to precision issues
    if (!transitions.empty()) {
        return {transitions.back().target_state, transitions.back().cost};
    }
    
    return {id, 0.0}; // Dead end fallback
}

MDP::MDP(int num_states) : N(num_states) {
    for (int i = 0; i < N; ++i) {
        states.emplace_back(i);
    }
}

void MDP::add_transition(int from, int to, double prob, double cost) {
    if (from >= 0 && from < N) {
        states[from].add_transition(to, prob, cost);
    }
}

double MDP::simulate_episode(std::mt19937& gen) const {
    int current_state = 0;
    double total_cost = 0.0;
    
    while (current_state != N - 1) {
        auto next = states[current_state].get_next_state_and_cost(gen);
        current_state = next.first;
        total_cost += next.second;
    }
    
    return total_cost;
}
