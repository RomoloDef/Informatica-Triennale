#ifndef CUSTOMER_HPP
#define CUSTOMER_HPP

#include "engine.hpp"

class Customer : public Node {
private:
    int product_id; // Also customer index i
    double a1, b1, a2, b2;
    double a3, b3, a4, b4;

public:
    Customer(Engine* eng, int id, int prod_id, double a1, double b1, double a2, double b2, double a3, double b3, double a4, double b4)
        : Node(eng, id), product_id(prod_id), a1(a1), b1(b1), a2(a2), b2(b2), a3(a3), b3(b3), a4(a4), b4(b4) {}

    void fire(double t);

    void push(const Message& m, double t) override;
    void processFinish(double t) override;
};

#endif
