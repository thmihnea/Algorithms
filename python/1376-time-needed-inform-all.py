from typing import List
from queue import Queue

class Graph(object):

    def __init__(self, v: int):
        self.v = v
        self.adj = [[] for _ in range(v)]

    def add_edge(self, v: int, w: int):
        self.adj[v].append(w)
    
    def size(self):
        return self.v
    
    def edges(self, v: int):
        return self.adj[v]

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph: Graph = Graph(n)
        for i in range(n):
            if i is headID:
                continue
            graph.add_edge(manager[i], i)
        
        q: Queue = Queue()
        visited: List[bool] = [False for _ in range(n)]
        q.put(headID)
        visited[headID] = True

        time: List[int] = [0 for _ in range(n)]
        max_t: int = 0

        while not q.empty():
            top = q.get()
            _t: int = informTime[top]
            for entry in graph.edges(top):
                if not visited[entry]:
                    visited[entry] = True
                    time[entry] = time[top] + _t
                    max_t = max(max_t, time[entry])
                    q.put(entry)
        
        return max_t