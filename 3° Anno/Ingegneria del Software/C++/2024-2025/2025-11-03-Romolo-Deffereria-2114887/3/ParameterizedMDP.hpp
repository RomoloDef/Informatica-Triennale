#ifndef PARAMETERIZED_MDP_HPP
#define PARAMETERIZED_MDP_HPP

#include "MDP.hpp"

class ParameterizedMDP : public MDP {
private:
    double cost_00;
    double cost_01;
    double p;

public:
    ParameterizedMDP(int num_states, double c00, double c01);
    
    void set_p(double new_p);
    
    // Override simulate_episode to handle state 0 specifically
    double simulate_episode(std::mt19937& gen) const override;
};

#endif // PARAMETERIZED_MDP_HPP
