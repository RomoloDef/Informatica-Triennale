#include <iostream>
#include <fstream>
#include <vector>
#include <random>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

struct Drone {
    double x;
    double y;
    double z;
    bool active;
};

double distance(const Drone& a, const Drone& b) {
    return sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2) + pow(a.z - b.z, 2));
}

int main() {
    ifstream infile("parameters.txt");
    if (!infile) {
        cerr << "Error opening parameters.txt" << endl;
        return 1;
    }

    string dump;
    int H, N;
    double alpha, R;
    double X1, X2, Y1, Y2, Z1, Z2;
    
    infile >> dump >> H;
    infile >> dump >> N;
    infile >> dump >> alpha;
    infile >> dump >> R;
    infile >> X1 >> X2 >> Y1 >> Y2 >> Z1 >> Z2;
    infile.close();

    mt19937 gen(42);
    uniform_real_distribution<double> dis_x(X1, X2);
    uniform_real_distribution<double> dis_y(Y1, Y2);
    uniform_real_distribution<double> dis_z(Z1, Z2);
    uniform_real_distribution<double> dis_v(-alpha, alpha);

    vector<Drone> drones(N);
    for (int i = 0; i < N; ++i) {
        drones[i].x = dis_x(gen);
        drones[i].y = dis_y(gen);
        drones[i].z = dis_z(gen);
        drones[i].active = true;
    }

    for (int t = 1; t <= H; ++t) {
        // Move active drones
        for (int i = 0; i < N; ++i) {
            if (!drones[i].active) continue;
            double vx = dis_v(gen);
            double vy = dis_v(gen);
            double vz = dis_v(gen);
            drones[i].x = min(X2, max(X1, drones[i].x + vx));
            drones[i].y = min(Y2, max(Y1, drones[i].y + vy));
            drones[i].z = min(Z2, max(Z1, drones[i].z + vz));
        }

        // Check collisions
        vector<bool> to_remove(N, false);
        for (int i = 0; i < N; ++i) {
            if (!drones[i].active) continue;
            for (int j = i + 1; j < N; ++j) {
                if (!drones[j].active) continue;
                if (distance(drones[i], drones[j]) <= R) {
                    to_remove[i] = true;
                    to_remove[j] = true;
                }
            }
        }
        for (int i = 0; i < N; ++i) {
            if (to_remove[i]) drones[i].active = false;
        }
    }

    int Q = 0;
    for (int i = 0; i < N; ++i) {
        if (drones[i].active) Q++;
    }

    ofstream outfile("results.txt");
    if (!outfile) {
        cerr << "Error opening results.txt" << endl;
        return 1;
    }
    
    outfile << "2025-03-21-Romolo-Deffereria-2114887\n";
    outfile << "Q " << Q << "\n";
    outfile << "N " << N << "\n";
    outfile << "P " << (double)Q / N << "\n";
    outfile.close();

    return 0;
}
