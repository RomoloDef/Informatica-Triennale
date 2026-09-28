#ifndef SERVER_HPP
#define SERVER_HPP

#include <vector>
#include <queue>
#include <random>

class Server {
private:
    int id;
    std::vector<int> db;
    std::queue<int> fifo;
    double busy_timer;
    double F;
    double G;
    double p;
    int Q;

public:
    Server(int id, int N, int K, double F, double G, double p, int Q, std::mt19937& gen);
    
    void push_request(int product_id);
    
    // Returns product_id (success) or -product_id (failure).
    // Returns 0 if busy or empty.
    int step(double T, std::mt19937& gen);
};

#endif // SERVER_HPP
