class AIB {
public:
    AIB(const int& _n = 0) : n(_n) {
        aib = vector<int>(n + 1);
    }
    inline void Update(const int& pos, const int& val) {
        if (pos)
            for (int i = pos; i <= n; i += i & -i)
                aib[i] += val;
        return;
    }
    inline int Query(const int& pos) const {
        int sum(0);
        for (int i = pos; i > 0; i -= i & -i)
            sum += aib[i];
        return sum;
    }
private:
    int n;
    vector<int> aib;
};
class Multiset {
public:
    Multiset(const int& _n = 0) : n(_n), aib(n)
    {}
    inline void Insert(const int& val) {
        aib.Update(val, 1);
        return;
    }
    inline void Erase(const int& pos) {
        aib.Update(Find(pos), -1);
        return;
    }
    inline int Find(const int& pos) const {
        int st(1), dr(n), mid, res(0);
        while (st <= dr) {
            mid = (st + dr) / 2;
            if (aib.Query(mid) >= pos)
                res = mid, dr = mid - 1;
            else st = mid + 1;
        }
        return res;
    }
private:
    int n;
    AIB aib;
};
