from queue import Queue
from queue import LifoQueue

class DiGraph(object):

    def __init__(self, v: int):
        self.v = v
        self.adj = [[] for _ in range(v)]
        self.in_degree = [0 for _ in range(v)]
        self.out_degree = [0 for _ in range(v)]
    
    def size(self):
        return self.v

    def add_edge(self, v: int, w: int):
        self.adj[v].append(w)
        self.out_degree[v] += 1
        self.in_degree[w] += 1

    def edges(self, v: int):
        return self.adj[v]
    
    def in_degree(self, v: int):
        return self.in_degree[v]
    
    def out_degree(self, v: int):
        return self.out_degree[v]
    
def dfs(g: DiGraph, start: int):
    visited = [False for _ in range(g.size())]

    def _dfs(x: int):
        visited[x] = True
        print(x)
        for entry in g.edges(x):
            if not visited[entry]:
                _dfs(entry)
    
    _dfs(start)

def bfs(g: DiGraph, start: int):
    q = Queue()
    visited = [False for _ in range(g.size())]
    distance = [0 for _ in range(g.size())]
    q.put(start)
    visited[start] = True
    while not q.empty():
        top = q.get()
        print(top)
        for entry in g.edges(top):
            if not visited[entry]:
                q.put(entry)
                visited[entry] = True
                distance[entry] = 1 + distance[top]

def top_sort(g: DiGraph):
    # Reverse post-order of a DAG performs
    # a topological sort of its elements.
    visited = [False for _ in range(g.size())]
    stack = LifoQueue()

    def _dfs(x: int):
        visited[x] = True
        for entry in g.edges(x):
            _dfs(entry)
        stack.put(x)
    
    for i in range(g.size()):
        if not visited[i]:
            _dfs(i)
    
    print(stack)

if __name__ == '__main__':
    g = DiGraph(13)
    g.add_edge(4, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 2)
    g.add_edge(6, 0)
    g.add_edge(0, 1)
    g.add_edge(2, 0)
    g.add_edge(11, 12)
    g.add_edge(12, 9)
    g.add_edge(9, 10)
    g.add_edge(9, 11)
    g.add_edge(8, 9)
    g.add_edge(10, 12)
    g.add_edge(11, 4)
    g.add_edge(4, 3)
    g.add_edge(3, 5)
    g.add_edge(6, 8)
    g.add_edge(8, 6)
    g.add_edge(5, 4)
    g.add_edge(0, 5)
    g.add_edge(6, 4)
    g.add_edge(6, 9)
    g.add_edge(7, 6)
    bfs(g, 0)
    