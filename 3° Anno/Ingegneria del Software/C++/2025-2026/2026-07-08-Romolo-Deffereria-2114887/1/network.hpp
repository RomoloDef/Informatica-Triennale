#ifndef NETWORK_HPP
#define NETWORK_HPP

#include "uav.hpp"
#include <vector>

class Network {
private:
    std::vector<UAV> uavs;
    int N;
    int K;
    double L;

public:
    Network();
    void init(int N, int K, double L, std::mt19937& gen);

    void step(double V, double T, double PFAIL, double PREC, std::mt19937& gen);


    int coverage(double r, int h, int k) const;


    double avgCoverage(double r) const;


    double stdDevCoverage(double r) const;

    int getN() const { return N; }
    int getK() const { return K; }
    double getL() const { return L; }
};

#endif
