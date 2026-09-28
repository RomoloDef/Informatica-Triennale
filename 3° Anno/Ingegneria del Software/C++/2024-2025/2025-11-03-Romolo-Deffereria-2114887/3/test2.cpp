#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    ifstream infile("parameters.txt");
    string type;
    int N = 0, M = 0, B = 0;
    double K_cost = 0.0, c00 = 0.0, c01 = 0.0;
    
    while (infile >> type) {
        if (type == "N") infile >> N;
        else if (type == "M") infile >> M;
        else if (type == "B") infile >> B;
        else if (type == "K") infile >> K_cost;
        else if (type == "A") {
            int i, j; double p, c;
            infile >> i >> j >> p >> c;
            if (i == 0 && j == 0) c00 = c;
            else if (i == 0 && j == 1) c01 = c;
        }
    }
    cout << "N: " << N << " M: " << M << " B: " << B << " K: " << K_cost << endl;
    return 0;
}
