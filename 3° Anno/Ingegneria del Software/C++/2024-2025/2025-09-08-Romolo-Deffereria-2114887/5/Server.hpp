#ifndef SERVER_HPP
#define SERVER_HPP

#include <vector>
#include <queue>
#include <random>

struct CustomerRequest {
    int customer_id;
    int product_id;
};

class Server {
private:
    int id;
    std::vector<int> db;
    std::queue<CustomerRequest> customer_fifo;
    std::queue<int> provider_fifo;

public:
    Server(int id, int P, int K, std::mt19937& gen);
    
    void push_customer_request(int customer_id, int product_id);
    void push_provider_restock(int product_id);
    
    // Returns a list of {customer_id, response_msg}
    std::vector<std::pair<int, int>> step();
};

#endif // SERVER_HPP
