#ifndef NETWORK_HPP
#define NETWORK_HPP

#include "common.hpp"

class NetworkNode : public Node {
private:
    double r;
public:
    NetworkNode(Engine* eng, int id, double r) : Node(eng, id), r(r) {}
    void push(const Message& m, double t) override;
    void processFinish(double t) override;
};

#endif
