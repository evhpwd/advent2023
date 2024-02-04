#include <iostream>
#include <fstream>
#include <string>
#include <tuple>
#include <vector>
using namespace std;

struct Equation {
    tuple<float, float> pos;
    tuple<float, float> vel;
    float m;
    float c;
};

bool findIntersection(Equation eq1, Equation eq2) {
    auto low = 200000000000000;
    auto high = 400000000000000;

    if (eq1.m == eq2.m) {
        return false;
    }
    else {
        auto a1 = eq1.m; auto b1 = -1; auto c1 = eq1.c;
        auto a2 = eq2.m; auto b2 = -1; auto c2 = eq2.c;

        auto x = (b1 * c2 - b2 * c1) / (a1 * b2 - a2 * b1);
        auto y = (c1 * a2 - c2 * a1) / (a1 * b2 - a2 * b1);

        if (x >= low && x <= high && y >= low && y <= high) {
            auto vel1 = get<0>(eq1.vel); auto pos1 = get<0>(eq1.pos);
            auto vel2 = get<0>(eq2.vel); auto pos2 = get<0>(eq2.pos);

            if (((vel1 > 0 && x >= pos1) or (vel1 < 0 && x <= pos1)) &&
                ((vel2 > 0 && x >= pos2) or (vel2 < 0 && x <= pos2))) {
                return true;
            }
        }
        return false;
    }
}

tuple<float, float> numsFromString(string input) {
    float num1 = stof(input.substr(0, input.find(", ")));
    input = input.substr(input.find(", ")+2, input.length());
    float num2 = stof(input.substr(0, input.find(", ")));
    return { num1, num2 };

}

int main() {
    ifstream input;
	input.open("input24.txt");

    if (input.is_open()) {
        string line;
        vector<Equation> equations;

        while (getline(input, line)) {
            string stone[2] = {(line.substr(0, line.find('@'))), (line.substr(line.find('@') + 2, line.length()))};
            auto pos = numsFromString(stone[0]);
            auto vel = numsFromString(stone[1]);

            float m = get<1>(vel) / get<0>(vel);
            float c = -(m * get<0>(pos)) + get<1>(pos);

            equations.push_back({pos, vel, m, c});
        }
        input.close();

        int total = 0;
        for (auto it = equations.begin(); it != equations.end(); ++it) {
            for (auto after = it + 1; after != equations.end(); ++after) {
                if (findIntersection(*it, *after)) {
                    total++;
                }
            }
        }
        cout << total;
    }

    else cout << "Unable to open file";

}