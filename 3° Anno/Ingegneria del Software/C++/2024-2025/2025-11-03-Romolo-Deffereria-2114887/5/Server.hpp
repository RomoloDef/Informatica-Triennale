#ifndef SERVER_HPP
#define SERVER_HPP

#include <vector>
#include <queue>
#include <random>

class Server {
private:
    std::vector<int> db;
    std::queue<int> customer_fifo;
    double V;
    double W;
    int K;
    double p;
    std::mt19937 gen;
    double tau;
    double time_since_last_proc;

public:
    Server(int P, int K, double v, double w, double prob, int seed);
    
    void push_customer_request(int product_id);
    
    // Returns 0 if no response, or msg (j or -j)
    int step(double T);
};

#endif // SERVER_HPP
