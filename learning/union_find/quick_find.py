from typing import List

class UnionFind(object):
    # Defines the UnionFind data structures.
    # This implements the quick find algorithm (naive).
    
    def __init__(self, n: int):
        # Initialize a list of IDs. This will construct
        # 'n' separate objects with no external connections.
        self._id: List[int] = [i for i in range(n)]
        self._size = n
    
    def connected(self, p: int, q: int) -> bool:
        # If two components are connected, then
        # they have the same ID.
        return self._id[p] == self._id[q]
    
    def union(self, p: int, q: int):
        # Pick out the IDs of both components.
        _id_p: int = self._id[p]
        _id_q: int = self._id[q]
        for i in range(self._size):
            # Change all IDs that match p's ID
            # to the ID of q. Hence, all elements
            # that are connected to p, also get connected to q.
            if self._id[i] == _id_p:
                self._id[i] = _id_q