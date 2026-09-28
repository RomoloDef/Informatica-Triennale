#ifndef SUPPLIER_HPP
#define SUPPLIER_HPP

class Network;

class Supplier {
    int id;
    Network* net;
    double timer;
    double V, W;
    int S, P, Q;
public:
    Supplier(int id, Network* net, double V, double W, int S, int P, int Q);
    void update(double T);
};

#endif
