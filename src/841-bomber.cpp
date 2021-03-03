#include <fstream>
#include <cmath>
using namespace std;

ifstream cin("bomber.in");
ofstream cout("bomber.out");

int n , I;

struct shen
{
    int x , y , p;
}v[101];

bool puscate[101];

int dist(int a , int b , int c , int d)
{
    return sqrt((a - c) * (a - c) + (b - d) * (b - d));
}

void pusc(int i , int j , int putere , int q)
{
    puscate[q]=1;
    for(int k = 1 ; k <= n ; ++k)
    {
        if(dist(v[k].x , v[k].y , i , j) <= putere && k!=q && puscate[k]==0)
            pusc(v[k].x , v[k].y , v[k].p , k);
    }
}

int main()
{
    cin >> n >> I;
    for(int i = 1 ; i <= n ; ++i)
        cin >> v[i].x >> v[i].y >> v[i].p;
    pusc(v[I].x , v[I].y , v[I].p , I);
    int cnt=0;
    for(int i = 1 ; i <= n ; ++i)
        if(puscate[i]==0)
            cnt++;
    cout << cnt;
    return 0;
}
