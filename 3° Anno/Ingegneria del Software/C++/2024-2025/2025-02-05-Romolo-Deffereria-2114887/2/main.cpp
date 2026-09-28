#include <iostream>
#include <fstream>
#include <vector>
#include <random>
#include <string>
#include <algorithm>

using namespace std;

struct Point {
    double x;
    double y;
};

int main() {
    ifstream infile("parameters.txt");
    if (!infile) {
        cerr << "Error opening parameters.txt" << endl;
        return 1;
    }

    string dump;
    double C;
    int H, N;
    double X1, X2, Y1, Y2;
    int M;
    
    infile >> dump >> C;
    infile >> dump >> H;
    infile >> dump >> N;
    infile >> X1 >> X2 >> Y1 >> Y2;
    infile >> dump >> M;
    
    vector<Point> monitor_points(M);
    for (int i = 0; i < M; ++i) {
        infile >> monitor_points[i].x >> monitor_points[i].y;
    }
    infile.close();

    mt19937 gen(42);
    uniform_real_distribution<double> dis_x(X1, X2);
    uniform_real_distribution<double> dis_y(Y1, Y2);
    uniform_real_distribution<double> dis_v(-0.5, 0.5);

    int num_simulations = 1000;
    int success_count = 0;

    for (int sim = 0; sim < num_simulations; ++sim) {
        vector<Point> drones(N);
        for (int i = 0; i < N; ++i) {
            drones[i].x = dis_x(gen);
            drones[i].y = dis_y(gen);
        }

        vector<double> coverage_sum(M, 0.0);

        for (int t = 0; t < H; ++t) {
            // Compute q(x,y,t)
            for (int i = 0; i < M; ++i) {
                int q = 0;
                double px = monitor_points[i].x;
                double py = monitor_points[i].y;
                for (int d = 0; d < N; ++d) {
                    if (drones[d].x >= px - 1.0 && drones[d].x <= px + 1.0 &&
                        drones[d].y >= py - 1.0 && drones[d].y <= py + 1.0) {
                        q++;
                    }
                }
                coverage_sum[i] += q;
            }

            // Move drones
            for (int d = 0; d < N; ++d) {
                double vx = dis_v(gen);
                double vy = dis_v(gen);
                drones[d].x = min(X2, max(X1, drones[d].x + vx));
                drones[d].y = min(Y2, max(Y1, drones[d].y + vy));
            }
        }

        bool all_above_c = true;
        for (int i = 0; i < M; ++i) {
            if (coverage_sum[i] / H < C) {
                all_above_c = false;
                break;
            }
        }
        if (all_above_c) {
            success_count++;
        }
    }

    ofstream outfile("results.txt");
    if (!outfile) {
        cerr << "Error opening results.txt" << endl;
        return 1;
    }
    
    outfile << "2025-02-05-Romolo-Deffereria-2114887\n";
    outfile << "P " << (double)success_count / num_simulations << "\n";
    outfile.close();

    return 0;
}
