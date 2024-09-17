from typing import List
import queue

class Graph(object):
    
    def __init__(self, V: int):
        self.V = V
        self.adj: List[List[int]] = [[] for _ in range(V)]

    def size(self):
        return self.V
    
    def add_edge(self, v: int, w: int):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def edges(self, v: int) -> List[int]:
        return self.adj[v]

    def degree(self, v: int) -> int:
        return len(self.adj[v])
    
def dfs(g: Graph, start: int):
    visited = {i : False for i in range(g.size())}

    def _dfs(x: int):
        nonlocal g, visited
        visited[x] = True
        print(x)
        for entry in g.edges(x):
            if not visited[entry]:
                _dfs(entry)
    
    _dfs(start)

def marked(g: Graph):
    result = {i : 0 for i in range(g.size())} # Initialize as uncolored.
    to_process = set([i for i in range(g.size())]) 
    color = 0

    def _dfs(x: int):
        to_process.remove(x)
        result[x] = color

        for entry in g.edges(x):
            if entry in to_process:
                _dfs(entry)

    while len(to_process) > 0:
        color += 1
        item = next(iter(to_process))
        _dfs(item)
    
    return result

def bfs(g: Graph, start: int):
    visited = {i : False for i in range(g.size())}
    distance = {i : 0 for i in range(g.size())} # Distance from start to node i.
    q = queue.Queue()
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

if __name__ == '__main__':
    g = Graph(3)
    g.add_edge(0, 1)
    # Path between u and v <=> table[u] == table[v]. (same color)
    t = marked(g)
    print(t)
