from queue import LifoQueue
from typing import List

class DirectedEdge(object):

    def __init__(self, v: int, w: int, weight: float):
        self.v = v
        self.w = w
        self.weight = weight

    def _from(self) -> int:
        return self.v
    
    def _to(self) -> int:
        return self.w
    
    def weight(self) -> float:
        return self.weight
    
class EdgeWeightedDigraph(object):

    def __init__(self, v: int):
        self.v = v
        self.adj = [[] for _ in range(v)]

    def add_edge(self, edge: DirectedEdge):
        v: int = edge._from()
        self.adj[v].append(edge)

    def edges(self, v: int) -> List[DirectedEdge]:
        return self.adj[v]
    
    def size(self) -> int:
        return self.v
    
class ShortestPath(object):

    def __init__(self, graph: EdgeWeightedDigraph, source: int):
        self.graph: EdgeWeightedDigraph = graph
        self.source: int = source
        self.dist_to: List[float | int] = [0 if i == source else float("inf") for i in range(graph.size())]
        self.edge_to: List[DirectedEdge] = [None for _ in range(graph.size())]

    def distance(self, v: int) -> float:
        return self.dist_to[v]
    
    def get_path(self, v: int) -> LifoQueue:
        # Returns a stack containing all the edges on
        # the path. Continuously popping the stack
        # will yield the correct path.
        stack = LifoQueue()
        edge: DirectedEdge = self.edge_to[v]
        while edge is not None:
            stack.put(edge)
            edge = self.edge_to[edge._from()]
        return stack