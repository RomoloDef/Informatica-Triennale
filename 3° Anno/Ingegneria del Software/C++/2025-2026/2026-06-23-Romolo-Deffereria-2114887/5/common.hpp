#ifndef COMMON_HPP
#define COMMON_HPP

#include <queue>
#include <random>

enum MessageType {
    MSG_CUST_TO_SERVER,
    MSG_SERVER_REPLY_CUST,
    MSG_SERVER_TO_SUPPLIER,
    MSG_SUPPLIER_TO_SERVER
};

enum NodeType {
    TYPE_NETWORK,
    TYPE_SERVER,
    TYPE_CUSTOMER,
    TYPE_SUPPLIER
};

struct Message {
    NodeType dst_type;
    int dst_id;
    MessageType msg_type;
    
    // Payload
    int i; // product index
    int q; // quantity
    int k; // items delivered
    double v; // unit cost
    double c; // supplier cost
    int customer_id;
};

class Engine;

class Node {
protected:
    Engine* engine;
    int id;
    std::queue<Message> q;
    bool busy;
public:
    Node(Engine* eng, int id) : engine(eng), id(id), busy(false) {}
    virtual ~Node() {}
    virtual void push(const Message& m, double t) = 0;
    virtual void processFinish(double t) = 0;
};

#endif
