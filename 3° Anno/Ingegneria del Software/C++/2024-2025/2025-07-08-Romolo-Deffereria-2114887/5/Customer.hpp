#ifndef CUSTOMER_HPP
#define CUSTOMER_HPP

#include <random>
#include <queue>

class Customer {
private:
    int N;
    int S;
    double A;
    double B;
    std::mt19937 gen;
    double tau;
    double time_since_last_req;
    
    long long total_missed_sales;
    long long messages_sent;
    long long messages_received;
    std::queue<int> response_fifo;

public:
    Customer(int n, int s, double a, double b, int seed);
    
    void receive_response(int msg);
    
    // Returns pair<target_server, product_id>. Returns {0, 0} if no request.
    std::pair<int, int> step(double T);
    
    long long get_missed_sales() const { return total_missed_sales; }
    long long get_messages_sent() const { return messages_sent; }
    long long get_messages_received() const { return messages_received; }
};

#endif // CUSTOMER_HPP
