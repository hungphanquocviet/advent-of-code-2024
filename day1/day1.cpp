#include <bits/stdc++.h>
using namespace std;

int main() {
    string filepath = "../test/input.txt";
    vector<string> a;

    ifstream file(filepath);
    string line;

    while (getline(file, line)) {
        a.push_back(line);
    }

    file.close();
    return 0;
}