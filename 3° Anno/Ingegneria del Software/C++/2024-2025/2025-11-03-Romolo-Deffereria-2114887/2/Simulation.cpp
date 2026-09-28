#include "Simulation.hpp"
#include <random>

Simulation::Simulation(int m_sims, const MDP& markov_process, double v_max, int random_seed)
    : M(m_sims), mdp(markov_process), vmax(v_max), seed(random_seed) {}

double Simulation::get_success_probability() {
    std::mt19937 gen(seed);
    int successes = 0;
    
    for (int i = 0; i < M; ++i) {
        double cost = mdp.simulate_episode(gen);
        if (cost <= vmax) {
            successes++;
        }
    }
    
    return (double)successes / M;
}
