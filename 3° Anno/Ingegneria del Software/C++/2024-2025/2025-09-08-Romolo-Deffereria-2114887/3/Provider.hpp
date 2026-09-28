#ifndef PROVIDER_HPP
#define PROVIDER_HPP

#include <random>
#include <vector>

class Provider {
private:
    double V;
    double Q;
    int S;
    int P;
    std::mt19937 gen;
    double gamma;
    double time_since_last_restock;

public:
    Provider(double v, double q, int s, int p, int seed);

    std::pair<int, int> step(double T); // Returns {target_server, product_id} or {0, 0}
};

#endif // PROVIDER_HPP
