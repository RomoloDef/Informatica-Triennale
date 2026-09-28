#include "server.hpp"

Server::Server() : id(0), product(0), working(true),
    working_end(0), failed_end(0),
    w_low(0), w_high(0), f_low(0), f_high(0), b_low(0), b_high(0) {}

void Server::init(int server_id, int P,
                  double a2, double b2, double a3, double b3,
                  double a4, double b4, double a5, double b5,
                  double a6, double b6, double a7, double b7,
                  std::mt19937& gen) {
    id = server_id;
    product = (server_id - 1) % P + 1;
    

    int s = server_id;
    w_low = a2 + b2 * s;
    w_high = a3 + b3 * s;
    f_low = a4 + b4 * s;
    f_high = a5 + b5 * s;
    b_low = a6 + b6 * s;
    b_high = a7 + b7 * s;
    

    working = true;
    std::uniform_real_distribution<double> dist_w(w_low, w_high);
    working_end = dist_w(gen);  
    failed_end = 0;
}

bool Server::isWorkingAt(double /*t*/) const {

    return working;
}

void Server::updateState(double t, std::mt19937& gen) {

    while (true) {
        if (working) {
            if (t >= working_end) {
                working = false;
                std::uniform_real_distribution<double> dist_f(f_low, f_high);
                failed_end = working_end + dist_f(gen);
            } else {
                break;
            }
        } else {
            if (t >= failed_end) {
                working = true;
                std::uniform_real_distribution<double> dist_w(w_low, w_high);
                working_end = failed_end + dist_w(gen);
            } else {
                break;
            }
        }
    }
}

double Server::getServiceTime(std::mt19937& gen) const {
    std::uniform_real_distribution<double> dist_b(b_low, b_high);
    return dist_b(gen);
}
