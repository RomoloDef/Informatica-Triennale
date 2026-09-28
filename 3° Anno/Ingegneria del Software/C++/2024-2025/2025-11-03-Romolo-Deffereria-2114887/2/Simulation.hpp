#ifndef SIMULATION_HPP
#define SIMULATION_HPP

#include "MDP.hpp"

class Simulation {
private:
    int M;
    const MDP& mdp;
    int seed;
    double vmax;

public:
    Simulation(int m_sims, const MDP& markov_process, double v_max, int seed);
    double get_success_probability();
};

#endif // SIMULATION_HPP
