#ifndef NETWORK_HPP
#define NETWORK_HPP

#include <vector>

class Customer;
class Supplier;
class Server;

class Network {
    std::vector<Customer*> customers;
    std::vector<Supplier*> suppliers;
    std::vector<Server*> servers;
    int missed_sales;
public:
    Network();
    ~Network();
    void add_customer(Customer* c);
    void add_supplier(Supplier* s);
    void add_server(Server* s);
    
    void send_customer_req(int cust_id, int server_id, int product_i, int quantity_q);
    void send_supplier_req(int supp_id, int server_id, int product_i, int quantity_q);
    
    void log_missed_sale();
    int get_missed_sales() const { return missed_sales; }
    
    void step(double T);
};

#endif
