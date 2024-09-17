class DirectedEdge(object):

    def __init__(self, v: int, w: int, weight: float):
        self.v = v
        self.w = w
        self.weight = weight

    def _from(self):
        return self.v
    
    def _to(self):
        return self.w
    
    def weight(self):
        return self.weight
    
class EdgeWeightedDigraph(object):

    def __init__(self, v: int):
        self.v = v
        self.adj = [[] for _ in range(v)]

    def add_edge(self, edge: DirectedEdge):
        v: int = edge._from()
        self.adj[v].append(edge)

    def edges(self, v: int):
        return self.adj[v]
    
class ShortestPath(object):

    def __init__(self, graph: EdgeWeightedDigraph, source: int):
        self.graph = graph
        self.source = source