#ifndef SERVER_HPP
#define SERVER_HPP

#include <vector>
#include <queue>

class Network;

struct Msg {
    int type; // 0 for customer, 1 for supplier
    int sender_id;
    int product_i;
    int quantity_q;
};

class Server {
    int id;
    Network* net;
    std::vector<int> db;
    std::queue<Msg> fifo;
public:
    Server(int id, Network* net, int P, int Q);
    void receive_msg(const Msg& m);
    void update();
};

#endif
