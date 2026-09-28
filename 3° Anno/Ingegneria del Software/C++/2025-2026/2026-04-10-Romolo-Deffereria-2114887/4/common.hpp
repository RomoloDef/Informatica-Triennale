#ifndef COMMON_HPP
#define COMMON_HPP

#include <queue>
#include <vector>

enum MsgType {
    MSG_CUST_TO_SERVER,        // customer sends (i, q) to server
    MSG_SERVER_REPLY_CUST,     // server replies (i, k, v) to customer
    MSG_SERVER_TO_DB,          // server requests (i, q) from DB for cache update
    MSG_DB_REPLY_SERVER,       // DB replies (i, k, v) to server
    MSG_SUPPLIER_TO_DB,        // supplier sends (i, q) to DB
    MSG_DB_ACK_SUPPLIER        // DB sends ack to supplier
};

enum DstType {
    TYPE_NETWORK,
    TYPE_SERVER,
    TYPE_DB,
    TYPE_CUSTOMER,
    TYPE_SUPPLIER
};

struct Message {
    DstType dst_type = TYPE_NETWORK;
    int dst_id = 0;
    MsgType msg_type = MSG_CUST_TO_SERVER;

    int c = 0;     // customer id
    int s = 0;     // server id
    int i = 0;     // product id
    int q = 0;     // quantity requested
    int k = 0;     // quantity delivered
    double v = 0;  // unit cost
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
    virtual ~Node() = default;

    virtual void push(const Message& m, double t) = 0;
    virtual void processFinish(double t) = 0;
};

#endif
