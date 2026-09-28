#ifndef CUSTOMER_HPP
#define CUSTOMER_HPP

#include <vector>
#include <random>

class Customer {
private:
    int id;
    int state;
    int V;
    std::vector<int> products;
    double tau_low, tau_high;
    double cycle_start_time;
    double total_cycle_time;
    int completed_cycles;

public:
    Customer();
    void init(int customer_id, int V, int P,
              double a1, double b1, double a2, double b2,
              std::mt19937& gen);

    int getId() const { return id; }
    int getState() const { return state; }
    int getV() const { return V; }
    int getProductAt(int j) const { return products[j - 1]; }
    double getTau(std::mt19937& gen) const;
    void transitionToNextState();
    void startNewCycle(double t);
    void completeCycle(double t);
    double getAverageCycleTime() const;
    int getCompletedCycles() const { return completed_cycles; }
    const std::vector<int>& getProducts() const { return products; }
};

#endif
