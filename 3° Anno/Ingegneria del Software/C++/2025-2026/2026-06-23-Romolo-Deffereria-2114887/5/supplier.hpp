#ifndef SUPPLIER_HPP
#define SUPPLIER_HPP

#include "engine.hpp"

class Supplier : public Node {
private:
    double a5, b5;

public:
    Supplier(Engine* eng, int id, double a5, double b5)
        : Node(eng, id), a5(a5), b5(b5) {}

    void push(const Message& m, double t) override;
    void processFinish(double t) override;
};

#endif
