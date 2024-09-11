from typing import List

class UnionFind(object):
    # This class implements UnionFind using 
    # quick union. We use a parent array to hold
    # the required data. We also use weighting to
    # balance the trees.
    # Note: Smaller trees always go below
    # the larger trees.

    def __init__(self, n: int):
        self._parent = [i for i in range(n)]
        self._size = [1 for i in range(n)]
    
    def _get_root(self, entry: int):
        # Note that an entry is a root if it
        # is a parent to itself. Hence,
        # parent(x) = x must be satisfied.
        while self._parent[entry] != entry:
            # Path compression. Set the parent of an entry to 
            # its grandparent in order to flatten the tree.
            # If we have 1 -> 2 -> 3, we can simply redo this as
            # 1 -> 3 and 2 -> 3. We effectively flatten the tree.
            self._parent[entry] = self._parent[self._parent[entry]]
            entry = self._parent[entry]
        return entry
    
    def connected(self, p: int, q: int):
        # Check that they have the same root.
        return self._get_root(p) == self._get_root(q)

    def union(self, p: int, q: int):
        # To perform a union, set the root of
        # p to be a child of the root of q.
        root_p: int = self._get_root(p)
        root_q: int = self._get_root(q)
        if (root_p == root_q):
            return # Already connected.
        if self._size[root_p] < self._size[root_q]:
            self._parent[root_p] = root_q
            self._size[root_q] += self._size[root_p]
        else:
            self._parent[root_q] = root_p
            self._size[root_p] += self._size[root_q]