#include <fstream>
#include <algorithm>
using namespace std;

ifstream cin("sort_div.in");
ofstream cout("sort_div.out");

int n;
struct poz
{
    int val , nrdiv , control , primacif;
}a[10001];

int div(int n)
{
    int d = 2 , P = 1;
    while(n > 1)
    {
        int p = 0;
        while(n % d == 0) p++ , n /= d;
        if(p) P *= (p + 1);
        d++;
        if(d * d > n) d = n;
    }
    return P;
}

int Pcif(int n)
{
    while(n > 9) n /= 10;
    return n;
}

int comp(poz a , poz b)
{
    if(a.nrdiv < b.nrdiv) return 1;
    else if(a.nrdiv == b.nrdiv && a.control < b.control) return 1;
    else if(a.nrdiv == b.nrdiv && a.control == b.control && a.primacif < b.primacif) return 1;
    else if(a.nrdiv == b.nrdiv && a.control == b.control && a.primacif == b.primacif && a.val < b.val) return 1;
    else return 0;
}

int main()
{
    cin >> n;
    for(int i = 1 ; i <= n ; i++)
    {
        cin >> a[i].val;
        a[i].nrdiv = div(a[i].val);
        a[i].control = a[i].val % 9;
        if(a[i].control == 0) a[i].control = 9;
        a[i].primacif = Pcif(a[i].val);
    }
    sort(a + 1 , a + n + 1 , comp);
    for(int i = 1 ; i <= n ; i++)
        cout << a[i].val << " ";
}
