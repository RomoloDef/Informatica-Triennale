#ifndef COMMON_HPP
#define COMMON_HPP

#include <queue>
#include <vector>

enum MsgType {
    MSG_CUST_REQ,
    MSG_SERV_QUERY,
    MSG_DB_REPLY,
    MSG_SERV_UPDATE,
    MSG_SERV_REPLY_CUST,
    MSG_SUPP_RESTOCK
};

enum DstType {
    TYPE_NETWORK,
    TYPE_SERVER,
    TYPE_DB,
    TYPE_CUSTOMER
};

struct Message {
    DstType dst_type = TYPE_NETWORK;
    int dst_id = 0;
    MsgType msg_type = MSG_CUST_REQ;
    
    int c = 0; // customer id
    int s = 0; // server id
    int i = 0; // product id
    int q = 0; // quantity
    int g = 0; // available quantity
    int k = 0; // update quantity
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
