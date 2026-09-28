#include "Network.hpp"
#include "Customer.hpp"
#include "Supplier.hpp"
#include "Server.hpp"

Network::Network() : missed_sales(0) {}

Network::~Network() {
    for (auto c : customers) delete c;
    for (auto s : suppliers) delete s;
    for (auto s : servers) delete s;
}

void Network::add_customer(Customer* c) { customers.push_back(c); }
void Network::add_supplier(Supplier* s) { suppliers.push_back(s); }
void Network::add_server(Server* s) { servers.push_back(s); }

void Network::send_customer_req(int cust_id, int server_id, int product_i, int quantity_q) {
    Msg m = {0, cust_id, product_i, quantity_q};
    servers[server_id - 1]->receive_msg(m);
}

void Network::send_supplier_req(int supp_id, int server_id, int product_i, int quantity_q) {
    Msg m = {1, supp_id, product_i, quantity_q};
    servers[server_id - 1]->receive_msg(m);
}

void Network::log_missed_sale() {
    missed_sales++;
}

void Network::step(double T) {
    for (auto c : customers) c->update(T);
    for (auto s : suppliers) s->update(T);
    for (auto s : servers) s->update();
}
