#ifndef NETWORK_HPP
#define NETWORK_HPP

#include "server.hpp"
#include "customer.hpp"
#include <vector>
#include <random>

class Network {
private:
    std::vector<Server> servers;
    std::vector<Customer> customers;
    int P, K, C, V;
    double r;

public:
    Network();
    void init(int P, int K, int C, int V, double r,
              double a1, double b1, double a2, double b2,
              double a3, double b3, double a4, double b4,
              double a5, double b5, double a6, double b6,
              double a7, double b7,
              std::mt19937& gen);

    void simulate(double H, std::mt19937& gen, double& R_H, std::vector<double>& Q,
                  const std::vector<std::vector<std::vector<double>>>& probs);

    void simulateUniform(double H, std::mt19937& gen, double& R_H, std::vector<double>& Q);

    std::vector<int> getServersForProduct(int p) const;
    int getP() const { return P; }
    int getK() const { return K; }
    int getC() const { return C; }
    int getV() const { return V; }
};

#endif
