#include <iostream>
#include <fstream>
#include <string>
#include <random>
#include <cmath>

using namespace std;

int main() {
    ifstream infile("parameters.txt");
    if (!infile) {
        cerr << "Error opening parameters.txt" << endl;
        return 1;
    }

    string dump;
    double avg, stddev;
    infile >> dump >> avg;
    infile >> dump >> stddev;
    infile.close();

    mt19937 gen(42);
    normal_distribution<double> dis(avg, stddev);

    double current_time = 0;
    double max_time = 1e6;
    
    double sum = 0;
    double sum_sq = 0;
    int count = 0;

    while (current_time < max_time) {
        double T = dis(gen);
        if (T < 1.0) T = 1.0; // minimum 1 second based on time step
        int wait_time = round(T);
        
        current_time += wait_time;
        if (current_time <= max_time) {
            sum += wait_time;
            sum_sq += (double)wait_time * wait_time;
            count++;
        }
    }

    double est_avg = 0, est_stddev = 0;
    if (count > 0) {
        est_avg = sum / count;
        // Sample standard deviation or population? Usually population is fine for large N
        double variance = (sum_sq / count) - (est_avg * est_avg);
        if (variance > 0) est_stddev = sqrt(variance);
    }

    ofstream outfile("results.txt");
    if (!outfile) {
        cerr << "Error opening results.txt" << endl;
        return 1;
    }
    outfile << "2025-01-09-Romolo-Deffereria-2114887\n";
    outfile << "Avg " << est_avg << "\n";
    outfile << "StdDev " << est_stddev << "\n";
    outfile.close();

    return 0;
}
