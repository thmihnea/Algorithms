#include <iostream>
#include <list>

using namespace std;

struct date {
    int year;
    int month;
    int day;
};

static bool is_older(date compared, date comparedTo) {
    if (compared.year < comparedTo.year) return true;
    else if (compared.year > comparedTo.year) return false;
    else {
        if (compared.month < comparedTo.month) return true;
        else if (compared.month > comparedTo.month) return false;
        else {
            if (compared.day < comparedTo.day) return true;
            else return false;
        }
    }
}

static bool is_younger(date compared, date comparedTo) {
    return (!(is_older(compared, comparedTo)));
}

int main(int argc, char* argv[]) {
    int n;
    std::cin >> n;
    date oldest{9999, 9999, 9999}; int oldest_i;
    date youngest{0, 0, 0}; int youngest_i;

    for (int i = 1; i <= n; i++) {
        date d{};
        cin >> d.year >> d.month >> d.day;
        if (is_older(d, oldest)) {
            oldest = d;
            oldest_i = i;
        }
        if (is_younger(d, youngest)) {
            youngest = d;
            youngest_i = i;
        }
    }

    cout << youngest_i << " " << oldest_i;

}
