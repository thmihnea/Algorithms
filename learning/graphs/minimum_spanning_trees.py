from typing import List 
import heapq

class UnionFind(object):

    def __init__(self, size: int):
        self._size = [1 for _ in range(size)]
        self._parent = [i for i in range(size)]

    def _get_root(self, entry: int) -> int:
        while entry is not self._parent[entry]:
            self._parent[entry] = self._parent[self._parent[entry]] # Path compression.
            entry = self._parent[entry]
        return entry
    
    def connected(self, p: int, q: int) -> bool:
        return self._get_root(p) is self._get_root(q)

    def union(self, p: int, q: int):
        root_p = self._get_root(p)
        root_q = self._get_root(q)
        if root_p is root_q:
            return # Already connected
        # Connect roots carefully to balance tree.
        if self._size[root_p] > self._size[root_q]:
            self._parent[root_q] = root_p
            self._size[root_p] += self._size[root_q]
        else:
            self._parent[root_p] = root_q
            self._size[root_q] += self._size[root_p]

class Edge(object):

    def __init__(self, v: int, w: int, weight: float):
        self.v = v
        self.w = w
        self.weight = weight
    
    def weight(self) -> float:
        return self.weight

    def either(self) -> int:
        return self.v
    
    def other(self, vertex: int) -> int:
        if vertex == self.v:
            return self.w
        else:
            return self.v
    
    def compare(self, other) -> int:
        if self.weight < other.weight():
            return -1
        elif self.weight > other.weight():
            return 1
        else:
            return 0

class Graph(object):

    def __init__(self, v: int):
        self.v = v
        self.adj = [[] for _ in range(v)]
        self.edge_list = []
    
    def add_edge(self, edge: Edge):
        v = edge.either()
        w = edge.other(v)
        self.adj[v].append(edge)
        self.adj[w].append(edge)
        self.edge_list.append(edge)
    
    def size(self) -> int:
        return self.v
    
    def edges(self, v: int) -> List[Edge]:
        return self.adj[v]
    
class MinimumSpanningTree(object):

    # Idea is to make a cut of the graph and
    # always choose the crossing edge with the
    # lowest weight.

    def __init__(self, graph: Graph):
        pass

    def edges(self) -> List[Edge]:
        pass

    def weight(self) -> float:
        pass
    
class KruskalMST(MinimumSpanningTree):

    # We take all edges in ascending weight order.
    # We then add each edge unless it creates a
    # cycle. This generates an MST.
    #
    # We need to use a min-oriented priority
    # queue to keep track of the edges in sorted
    # order. We also need to use a UnionFind data
    # structure in order to check if adding a certain
    # edge would result in a cycle.
    #
    # Using UF, a cycle results if we connect two
    # components which are already connected.
    
    def __init__(self, graph: Graph):
        self._graph: Graph = graph
        self._queue: List[Edge] = sorted(
            graph.edge_list(),
            key=lambda edge: edge.weight()
        )
        self._edges: List[Edge] = []

        uf: UnionFind = UnionFind(graph.size())
        while len(self._queue) > 0 and len(self._edges) < graph.size() - 1:
            edge: Edge  = self._queue.pop(0)
            v: int = edge.either()
            w: int = edge.other(v)
            if not uf.connected(v, w):
                uf.union(v, w)
                self._edges.insert(0, edge)
    
    def edges(self) -> List[Edge]:
        return self._edges
    
    def weight(self) -> float:
        return sum(entry.weight() for entry in self._edges)