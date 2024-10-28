from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Set: mask |= (1 << p)
        # Check: mask & (1 << p)
        visited = set()
        def dfs(mask, length):
            if length == k:
                visited.add(mask)
            else:
                for i in range(1, n + 1):
                    if not mask & (1 << i):
                        dfs(mask | (1 << i), length + 1)
        dfs(1 << (n + 1), 0)
        result = []
        for mask in visited:
            mapping = []
            for i in range(1, n + 1):
                if mask & (1 << i):
                    mapping.append(i)
            result.append(mapping)
        return result