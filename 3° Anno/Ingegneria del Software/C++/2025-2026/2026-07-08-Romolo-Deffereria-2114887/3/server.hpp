#ifndef SERVER_HPP
#define SERVER_HPP

#include <random>

class Server {
private:
    int id;           
    int product;      
    bool working;
    

    double working_end;  
    double failed_end;   


    double w_low, w_high;   
    double f_low, f_high;   
    double b_low, b_high;   

public:
    Server();
    void init(int server_id, int P,
              double a2, double b2, double a3, double b3,
              double a4, double b4, double a5, double b5,
              double a6, double b6, double a7, double b7,
              std::mt19937& gen);

    int getId() const { return id; }
    int getProduct() const { return product; }
    

    bool isWorkingAt(double t) const;
    

    void updateState(double t, std::mt19937& gen);
    

    double getServiceTime(std::mt19937& gen) const;
    

    double getWorkingEnd() const { return working_end; }
    double getFailedEnd() const { return failed_end; }
};

#endif
