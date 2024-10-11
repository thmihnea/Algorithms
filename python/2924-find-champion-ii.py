from typing import List

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        self.degree_in: List[int] = [0 for _ in range(n)]
        for entry in edges:
            self.degree_in[entry[1]] += 1
        found = False
        idx = -1
        for i in range(n):
            if self.degree_in[i] == 0:
                if found:
                    return -1
                found = True
                idx = i
        return idx
        