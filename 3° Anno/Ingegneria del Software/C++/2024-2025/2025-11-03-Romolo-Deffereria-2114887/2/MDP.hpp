#ifndef MDP_HPP
#define MDP_HPP

#include <vector>
#include <random>

struct Transition {
    int target_state;
    double probability;
    double cost;
};

class State {
private:
    int id;
    std::vector<Transition> transitions;

public:
    State(int id);
    void add_transition(int target, double prob, double cost);
    std::pair<int, double> get_next_state_and_cost(std::mt19937& gen) const;
};

class MDP {
protected:
    int N;
    std::vector<State> states;

public:
    MDP(int num_states);
    virtual ~MDP() = default;

    virtual void add_transition(int from, int to, double prob, double cost);
    
    // Returns total cost to reach state N-1 from state 0
    double simulate_episode(std::mt19937& gen) const;
};

#endif // MDP_HPP
