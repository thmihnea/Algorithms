from typing import List

class UnionFind(object):

    def __init__(self, size: int):
        self.parent: List[int] = [i for i in range(size)]
        self.size: List[int] = [1 for _ in range(size)]
        self.max: List[int] = [i for i in range(size)]
    
    def _get_root(self, entry: int) -> int:
        while entry != self.parent[entry]:
            self.parent[entry] = self.parent[self.parent[entry]]
            entry = self.parent[entry]
        return entry
    
    def connected(self, p: int, q: int) -> bool:
        return self._get_root(p) == self._get_root(q)
    
    def union(self, p: int, q: int):
        root_p: int = self._get_root(p)
        root_q: int = self._get_root(q)
        if root_p == root_q:
            return
        if self.size[root_p] > self.size[root_q]:
            self.parent[root_q] = root_p
            self.size[root_q] += self.size[root_p]
            self.max[root_p] = max(self.max[root_p], self.max[root_q])
        else:
            self.parent[root_p] = root_q
            self.size[root_p] += self.size[root_q]
            self.max[root_q] = max(self.max[root_p], self.max[root_q])
    
    def find(self, p: int) -> int:
        root = self._get_root(p)
        return self.max[root]

if __name__ == '__main__':
    uf = UnionFind(10)
    uf.union(1, 2)
    uf.union(6, 9)
    uf.union(2, 6)

    print(uf.connected(2, 6))
    print(uf.find(1))