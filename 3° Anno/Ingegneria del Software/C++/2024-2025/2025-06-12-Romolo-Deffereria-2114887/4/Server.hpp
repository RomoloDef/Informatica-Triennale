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

public:
    Server(int id, int N, int K, double F, std::mt19937& gen);
    
    void push_request(int product_id);
    void restock(int product_id, int amount);
    
    // Returns product_id if handled (positive for success, negative for failure).
    // Returns 0 if busy or empty.
    int step(double T);
};

#endif // SERVER_HPP
