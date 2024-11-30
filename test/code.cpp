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

    int res = 0;

    for (string& s : a) {
        char x, y;

        for (int i = 0; i < s.size(); i++) {
            if (isdigit(s[i])) {
                x = s[i];
                break;
            }
        }

        for (int i = s.size()-1; i >= 0; i--) {
            if (isdigit(s[i])) {
                y = s[i];
                break;
            }
        }

        string temp = "";
        temp += x;
        temp += y;

        res += stoi(temp);
    }

    cout << res << "\n";
    return 0;
}