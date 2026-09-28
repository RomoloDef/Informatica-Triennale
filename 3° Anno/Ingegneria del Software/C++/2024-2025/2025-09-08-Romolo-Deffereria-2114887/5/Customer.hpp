#ifndef CUSTOMER_HPP
#define CUSTOMER_HPP

#include <random>
#include <vector>

class Customer {
private:
    double A;
    double B;
    int S;
    int P;
    std::mt19937 gen;
    double tau;
    double time_since_last_req;

    long long missed_sales;

public:
    Customer(double a, double b, int s, int p, int seed);

    std::pair<int, int> step(double T); // Returns {target_server, product_id} or {0, 0}
    void receive_response(int msg);
    
    long long get_missed_sales() const { return missed_sales; }
};

#endif // CUSTOMER_HPP
