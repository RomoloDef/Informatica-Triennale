#ifndef SIMULATION_HPP
#define SIMULATION_HPP

#include "MDP.hpp"

class Simulation {
private:
    int M;
    const MDP& mdp;
    int seed;

public:
    Simulation(int m_sims, const MDP& markov_process, int seed);
    double get_expected_cost();
};

#endif // SIMULATION_HPP
