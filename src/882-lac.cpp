#include <fstream>
using namespace std;
ifstream cin("lac.in");
ofstream cout("lac.out");
const int di[]={-1 , 0 , 1 , 0};
const int dj[]={0 , 1 , 0 , -1};
int n , m , a[1002][1002] , x[1000001] , y[1000001];
int ip , jp , is , js;///coordonatele

bool inside(int i , int j)
{
    return i>=1 && i<=n && j>=1 && j<=m;
}
void lee(int ip , int jp)
{
    int st = 1 , dr = 1;
    a[ip][jp] = 2;
    x[1]=ip;
    y[1]=jp;
    while(st <= dr)
    {
        int i= x[st] , j = y[st];
        for(int k = 0 ; k < 4 ; k++)
        {
            int ii = i+di[k];
            int jj = j+dj[k];
            if(inside(ii , jj) && a[ii][jj]==1)
            {
                dr++;
                x[dr]=ii;
                y[dr]=jj;
                a[ii][jj]=2;
            }
        }
        st++;
    }
}
int main()
{
    int p = 0 , k = 0;
    cin >> n >> m;
    for(int i = 1 ; i <=n ; ++i)
        for(int j = 1 ; j <=m ; ++j)
            cin >> a[i][j];
    for(int i = 1 ; i <=n ; ++i)
    {
        if(a[i][1]==1){p++;lee(i,1);}
        if(a[i][m]==1){p++;lee(i,m);}
    }
    for(int i = 1 ; i <=m ; ++i)
    {
        if(a[1][i]==1){p++;lee(1,i);}
        if(a[n][i]==1){p++;lee(n,i);}
    }
    for(int i = 2 ; i <n ; ++i)
    {
        for(int j = 2 ; j <m ; ++j)
        {
            if(a[i][j]==1)
            {
                k++;
                lee(i,j);
            }
        }
    }
    cout << k << " "<<p;
    return 0;
}
