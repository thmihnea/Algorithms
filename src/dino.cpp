/*
 * Libraries.
 */
#include <fstream>
#include <cmath>
#include <vector>
#include <queue>

#define BIG 999999999

using namespace std;

ifstream cin("intrare.in");
ofstream cout("iesire.out");

static int mat[501][501], res[501][501];
static int m, n, D, S, k;

struct point {
public:
    int x;
    int y;
};

static vector<point> directions = {point{0, -1}, point{0, 1}, point{-1, 0}, point{1, 0}};
static vector<point> tarcuri = {};
static queue<point> q;

static bool is_in_mat(point p) {
    return p.x >= 1 && p.y >= 1 && p.x <= n && p.y <= m;
}

static int get_last_digits(int amount, int x) {
    int s = 0;
    int i = 1;
    while (i <= amount) {
        s *= 10;
        s += x % 10;
        x /= 10;
        i++;
    }
    return s;
}

static bool is_complementary(int s, int x1, int x2) {
    int last_s_digits_x1 = get_last_digits(s, x1);
    int last_s_digits_x2 = get_last_digits(s, x2);
    int should_be_equal_to = pow(10, s);
    return last_s_digits_x1 + last_s_digits_x2 == should_be_equal_to;
}

static void lee(point plecare) {
    q.push(plecare);
    res[plecare.x][plecare.y] = 1;
    while (!(q.empty())) {
        point front = q.front();
        q.pop();
        for (auto &dir_point : directions) {
            point new_point = point{front.x + dir_point.x, front.y + dir_point.y};
            if (is_in_mat(new_point) && is_complementary(S, k, mat[new_point.x][new_point.y]) && res[new_point.x][new_point.y] == 0) {
                res[new_point.x][new_point.y] = res[front.x][front.y] + 1;
                q.push(new_point);
            }
        }
    }
}

static int compute_minimum_distance() {
    int minimum_distance = BIG;
    for (auto &tarc : tarcuri) {
        int value = res[tarc.x][tarc.y];
        if (value == 0) continue;
        if (value < minimum_distance) minimum_distance = value;
    }
    return minimum_distance;
}

static void display_result(int minimum_distance) {
    if (minimum_distance == BIG - 1)
        cout << "Dinozaurul nu a putut parcurge drumul pe nicaieri intrucat keycard-ul lui nu s-a potrivit cu nicio usa!";
    else
        cout << minimum_distance;
}

int main(int argc, char* argv[]) {
    cin >> n >> m >> D;
    int L, C;
    cin >> L >> C >> k >> S;
    for (int i = 1; i <= D; i++) {
        int x, y;
        cin >> x >> y;
        point tarc = {x, y};
        tarcuri.push_back(tarc);
    }
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++) {
            cin >> mat[i][j];
            res[i][j] = 0;
        }
    point plecare = {L, C};
    lee(plecare);
    int minimum_distance = compute_minimum_distance();
    display_result(minimum_distance);
}
