#ifndef CUSTOMER_HPP
#define CUSTOMER_HPP

class Network;

class Customer {
    int id;
    Network* net;
    double timer;
    double A, B;
    int S, P, Q;
public:
    Customer(int id, Network* net, double A, double B, int S, int P, int Q);
    void update(double T);
};

#endif
