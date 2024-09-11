from typing import List

class UnionFind(object):
    # This class implements UnionFind using 
    # quick union. We use a parent array to hold
    # the required data.

    def __init__(self, n: int):
        self._parent = [i for i in range(n)]
        self._size = n
    
    def _get_root(self, entry: int):
        # Note that an entry is a root if it
        # is a parent to itself. Hence,
        # parent(x) = x must be satisfied.
        while self._parent[entry] != entry:
            entry = self._parent[entry]
        return entry
    
    def connected(self, p: int, q: int):
        # Check that they have the same root.
        return self._get_root(p) == self._get_root(q)

    def union(self, p: int, q: int):
        # To perform a union, set the root of
        # p to be a child of the root of q.
        self._parent[self._get_root(p)] = self._get_root(q)