#include <iostream>
#include <fstream>
#include <string>
#include <random>
#include <vector>
#include <cmath>

using namespace std;

int main() {
    ifstream infile("parameters.txt");
    if (!infile) {
        cerr << "Error opening parameters.txt" << endl;
        return 1;
    }

    string dump;
    int N;
    double avg, stddev;
    infile >> dump >> N;
    infile >> dump >> avg;
    infile >> dump >> stddev;
    infile.close();

    mt19937 gen(42);
    normal_distribution<double> dis(avg, stddev);

    double max_time = 1e6;
    vector<int> counts(N, 0);
    int total_msgs = 0;

    for (int i = 0; i < N; ++i) {
        double current_time = 0;
        while (current_time < max_time) {
            double T = dis(gen);
            if (T < 1.0) T = 1.0;
            int wait_time = round(T);
            
            current_time += wait_time;
            if (current_time <= max_time) {
                counts[i]++;
                total_msgs++;
            }
        }
    }

    ofstream outfile("results.txt");
    if (!outfile) {
        cerr << "Error opening results.txt" << endl;
        return 1;
    }
    outfile << "2025-01-09-Romolo-Deffereria-2114887\n";
    for (int i = 0; i < N; ++i) {
        outfile << (i + 1) << " " << counts[i] << "\n";
    }
    outfile << "M1 " << total_msgs << "\n";
    outfile.close();

    return 0;
}
