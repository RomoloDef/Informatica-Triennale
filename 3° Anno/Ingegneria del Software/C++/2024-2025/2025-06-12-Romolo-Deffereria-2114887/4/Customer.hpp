#ifndef CUSTOMER_HPP
#define CUSTOMER_HPP

#include <random>

class Customer {
private:
    int N;
    double A;
    double B;
    std::mt19937 gen;
    double tau;
    double time_since_last_req;

public:
    Customer(int n, double a, double b, int seed);
    int step(double T);
};

#endif // CUSTOMER_HPP
