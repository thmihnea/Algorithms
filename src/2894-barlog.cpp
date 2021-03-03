#include <fstream>
#include <cstring>
#include <algorithm>
#include <queue>
using namespace std;

ifstream cin("barlog.in");
ofstream cout("barlog.out");

#define MaxN 101
#define Smax 21
#define Inf 0x3f3f3f

int cer, n, m, Xf, Yf;
bool ok[MaxN][MaxN];
char mat[MaxN][MaxN][Smax];
int dist[MaxN][MaxN] = {Inf} , nr;

struct poz
{
    int i , j;
};

const int di[] = {0, 0, 1, -1};
const int dj[] = {1, -1, 0, 0};

queue <poz>Q;
int inside(int i , int j)
{
    return i >= 1 && i <= n && j >= 1 && j <= m;
}

void lee(int i , int j)
{
    poz x;
    x.i = i;
    x.j = j;
    Q.push(x);
    nr++;
    dist[i][j] = 1;
    while(!Q.empty())
    {
        x = Q.front();
        for(int i = 0 ; i < 4 ; i++)
        {
            int inou = x.i + di[i];
            int jnou = x.j + dj[i];
            if(inside(inou , jnou) && ok[x.i][x.j] == 1 && dist[inou][jnou] == 0)
            {
                poz y;
                y.i = inou;
                y.j = jnou;
                Q.push(y);
                dist[inou][jnou] = dist[x.i][x.j] + 1;
                nr++;
            }
        }
        Q.pop();
    }
}

bool searchs(char a[], char b[])
{
    int i = 0, n = strlen(a);
    int indb = 0, lb = strlen(b);
    while (i < n)
    {
        if (a[i] == b[indb])i ++, indb ++;
        else i ++;
        if (indb == lb)return 1;
    }
    return 0;
}
int main()
{
    char cheie[Smax];

    cin >> cer >> n >> m;
    for (int i = 1; i <= n; ++ i)
        for (int j = 1; j <= m; ++ j)
            cin >> mat[i][j];

    cin >> Xf >> Yf;
    cin >> cheie;

    int nr1 = 0;
    for (int i = 1; i <= n; ++ i)
        for (int j = 1; j <= m; ++ j)
        {
            if (searchs(cheie, mat[i][j]))
            {
                ok[i][j] = 1;

            }
        }
        lee(Xf, Yf);
        int dmin = Inf;
        for(int i = 1; i <= n; ++ i)
        {
            if(dist[i][1] != 0 && ok[i][1] == 1)
                dmin = min(dmin, dist[i][1]);
            if(dist[i][m] != 0 && ok[i][m] == 1)
                dmin = min(dmin, dist[i][m]);
        }

        for (int i = 1; i <= m; ++ i)
        {
            if(dist[1][i] != 0 && ok[1][i] == 1)
                dmin = min(dmin, dist[1][i]);
            if(dist[n][i] != 0 && ok[n][i] == 1)
                dmin = min(dmin, dist[n][i]);
        }
    if(cer == 2)cout << dmin;
    else cout << nr;
    return 0;
}
