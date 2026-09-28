#ifndef SERVER_HPP
#define SERVER_HPP

#include "engine.hpp"
#include <map>

struct DBEntry {
    int g; // quantity
    double v; // unit cost
};

class ServerNode : public Node {
private:
    int P;
    int W;
    double tau0;
    double tau1;

    double sellBuy;
    std::map<int, DBEntry> db;

    std::vector<double> x;
    std::vector<double> y;
    std::vector<double> z;

public:
    ServerNode(Engine* eng, int id, int P, int W, double tau0, double tau1, double b5);

    void scheduleUpdate(double t);
    void doUpdate(double t);

    void push(const Message& m, double t) override;
    void processFinish(double t) override;

    double getSellBuy() const { return sellBuy; }
};

#endif
