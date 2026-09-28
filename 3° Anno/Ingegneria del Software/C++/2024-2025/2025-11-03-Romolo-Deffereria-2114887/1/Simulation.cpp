#include "Simulation.hpp"
#include <random>

Simulation::Simulation(int m_sims, const MDP& markov_process, int random_seed)
    : M(m_sims), mdp(markov_process), seed(random_seed) {}

double Simulation::get_expected_cost() {
    std::mt19937 gen(seed);
    double total_cost = 0.0;
    
    for (int i = 0; i < M; ++i) {
        total_cost += mdp.simulate_episode(gen);
    }
    
    return total_cost / M;
}
