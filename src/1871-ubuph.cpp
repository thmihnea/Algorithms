#include <fstream>
#include <queue>

#define BIG 10000000;

int mat[1001][1001];
int res[1001][1001];
int n, m;

struct point {
    int x;
    int y;
};

point dir[] = {point{0, -1}, point{0, 1}, point{-1, 0}, point{1, 0}};
std::queue<point> q;

bool inside(point p) {
    return p.x >= 1 && p.x <= n && p.y >= 1 && p.y <= m;
}

void lee(point p) {
    q.push(p);
    while (!(q.empty())) {
        point point_front = q.front();
        for (int i = 0; i <= 3; i++) {
            int x = point_front.x + dir[i].x;
            int y = point_front.y + dir[i].y;
            auto new_point = point{x, y};
            if (inside(new_point) && res[x][y] > mat[x][y] + res[point_front.x][point_front.y]) {
                q.push(new_point);
                res[x][y] = mat[x][y] + res[point_front.x][point_front.y];
            }
        }
        q.pop();
    }
}

std::ifstream cin("ubuph.in");
std::ofstream cout("ubuph.out");

int main(int argc, char* argv[]) {
    cin >> n >> m;
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++)
            cin >> mat[i][j];
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++)
            res[i][j] = BIG;
    int ic, jc, im, jm;
    cin >> im >> jm >> ic >> jc;
    point start = {ic, jc};
    res[ic][jc] = mat[ic][jc];
    lee(start);
    cout << res[im][jm];
}
