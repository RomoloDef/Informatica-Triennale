#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

struct Transition {
    int target_state;
    double probability;
    double cost;
};

int main() {
    ifstream infile("parameters.txt");
    string type;
    int N = 0;
    
    while (infile >> type) {
        if (type == "N") infile >> N;
        else if (type == "M") { int m; infile >> m; }
        else if (type == "B") { int b; infile >> b; }
        else if (type == "K") { double k; infile >> k; }
        else if (type == "A") {
            int i, j; double p, c;
            infile >> i >> j >> p >> c;
        }
    }
    
    vector<vector<Transition>> states(N);
    infile.clear();
    infile.seekg(0);
    while (infile >> type) {
        if (type == "A") {
            int i, j; double p, c;
            infile >> i >> j >> p >> c;
            if (i != 0) {
                states[i].push_back({j, p, c});
            }
        } else if (type == "N" || type == "M" || type == "B" || type == "K") {
            double val; infile >> val;
        }
    }
    for (int i=0; i<N; ++i) {
        cout << "State " << i << " transitions: ";
        for (auto t : states[i]) cout << "->" << t.target_state << "(" << t.probability << ") ";
        cout << endl;
    }
    return 0;
}
