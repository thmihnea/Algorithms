#include <fstream>
#include <queue>
#include <queue>
using namespace std;
ifstream cin("labirint.in");
ofstream cout("labirint.out");

int a[1001][1001] , b[1001][1001] , n , g;

int di[] = {-1 ,  0 , 0 , 1};
int dj[] = { 0 , -1 , 1 , 0};

struct poz
{
    int i,j;
};

queue<poz> q;

bool inside(int i,int j)
{
    return i > 0 && j > 0 && i <= n && j <= n;
}

int lee(poz start, int v)
{
    if(a[1][1] > v) return 0;
    for(int i = 1; i <= n; i++)
        for(int j = 1; j <= n; j++)
            b[i][j] = 0;
    q.push(start);
    b[1][1] = 1;
    while(!q.empty())
    {
        poz x = q.front();
        for(int d = 0; d < 4; d++)
        {
            int inou = x.i + di[d];
            int jnou = x.j + dj[d];
            if(inside(inou,jnou) && b[inou][jnou] == 0 && a[inou][jnou] <= v)
            {
                    b[inou][jnou] = b[x.i][x.j]+1;
                    q.push({inou , jnou});
            }
        }
        q.pop();
    }
    return b[n][n];
}

void cautabin(int st , int dr)
{
    poz x;
    x.i = 1;
    x.j = 1;
    while(st <= dr)
        {
            int mij = (st + dr)/2;
            if(lee(x , mij)) dr = mij - 1;
            else st = mij + 1;
        }
    cout << st;
}
int main()
{
    cin >> n;
    for(int i = 1; i <= n; i++)
        for(int j = 1; j <= n; j++)
            cin >> a[i][j];
    cautabin(1 , 100000);
    return 0;
}
