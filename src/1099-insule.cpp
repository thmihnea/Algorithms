#include <fstream>
using namespace std;
ifstream fin("insule.in");
ofstream fout("insule.out");
struct POZ{int lin;int col; } ;
int di[]={1,-1,0,0},
    dj[]={0,0,-1,1};
int n , m , A[101][101], Nr[4];
void Lee(int i, int j, int vv, int vn)
{
    POZ Q[10001];
    int st = 1, dr = 0;
    dr ++;
    Q[dr] = {i,j};
    A[i][j] = vn;
    while(st <= dr)
    {
        int i = Q[st].lin , j = Q[st].col;
        for(int k = 0 ; k < 4 ; k ++)
        {
            int iv = i + di[k], jv = j + dj[k];
            if(iv >= 1 && iv <= n && jv >= 1 && jv <= m && A[iv][jv] == vv)
            {
                dr ++;
                Q[dr] = {iv , jv};
                A[iv][jv] = vn;
            }
        }
        st ++;
    }
}
int LangaInsula(int i, int j, int tipInsula)
{
    if(i<1 || i > n || j < 1 || j > m) return 0;
    if(A[i][j] != 0) return 0;
    for(int k = 0 ; k < 4 ; k ++)
    {
        int iv , jv;
        iv = i + di[k];
        jv = j + dj[k];
        if(iv >= 1 && iv <= n && jv >= 1 && jv <= m && A[iv][jv] == tipInsula) return 1;
    }
    return 0;
}
int main()
{
    char c;
    fin >> n >> m;
    for(int i = 1; i <= n; i++)
        for(int j = 1; j <= m; j++)
        {
            fin >> c;
            A[i][j] = c-'0';
        }

    for(int i = 1 ; i <= n ; i ++)
        for(int j = 1 ; j <= m ; j ++)
            if(A[i][j] > 0)
            {
                Nr[A[i][j]] ++;
                Lee(i , j , A[i][j], -A[i][j] );
            }
    fout << Nr[1] << " " << Nr[2] << " " << Nr[3] << " ";
    POZ Q[10001];
    int st = 1 , dr = 0;
    for(int i = 1 ;i <= n ; i ++)
        for(int j = 1 ; j <= m ;j ++)
            if(LangaInsula(i , j , -1)){A[i][j] = 1;Q[++dr] = {i,j};}
    int rez = -1;
    while(st <= dr && rez == -1)
    {
        int i = Q[st].lin, j = Q[st].col;
        for(int k = 0 ; k < 4 && rez == -1 ; k ++)
        {
            int iv , jv;
            iv = i + di[k];
            jv = j + dj[k];
            if(iv >= 1 && iv <= n && jv >= 1 && jv <= m && A[iv][jv] == 0)
            {
                if(LangaInsula(iv,jv,-2))
                    rez = A[i][j] + 1;
                else
                {
                    A[iv][jv] = A[i][j] + 1;
                    Q[++dr] = {iv,jv};
                }
            }
        }
        st ++;
    }
    fout << rez;
    return 0;
}
