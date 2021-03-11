#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

static vector<string> v = {};
static int n, cerinta;
static string longest;

struct compare {
    inline bool operator()(const string &first, const string &second) const {
        return first.size() < second.size();
    }
};

static string lexicographic_compare(const string& first, const string& second) {
    for (int i = 0; i < first.length(); i++) {
        if (first.at(i) < second.at(i)) return first;
        else if (second.at(i) < first.at(i)) return second;
    }
    return first;
}

static bool contains(const string& s, const string& to_contain) {
    unordered_map<char, int> map = {};
    for (char c : s) map[c]++;
    for (char c : to_contain) {
        map[c]--;
        if (map[c] < 0) return false;
    }
    return true;
}

static vector<string> get_interesante() {
    compare c;
    sort(v.begin(), v.end(), c);
    vector<string> ret = {};
    for (int i = v.size() - 1; i >= 0; i--) {
        string s = v[i];
        bool ok = true;
        for (int j = i + 1; j < v.size(); j++)
            if (contains(v[j], s)) {
                ok = false;
                break;
            }
        if (ok) ret.push_back(s);
    }
    return ret;
}

void solve(int cerinta) {
    switch (cerinta) {
        case 1:
            cout << longest;
            break;
        case 2:
            for (auto &s : get_interesante())
                cout << s << endl;
            break;
    }
}

int main(int argc, char* argv[]) {
    cin >> cerinta >> n;
    for (int i = 0; i < n; i++) {
        string s; cin >> s;
        if (s.length() > longest.length())
            longest = s;
        else if (s.length() == longest.length())
            longest = lexicographic_compare(s, longest);
        v.push_back(s);
    }
    solve(cerinta);
}
