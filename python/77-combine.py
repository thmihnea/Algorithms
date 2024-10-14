from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # set bit at position p: mask |= (1 << p)
        # unset: mask &= ˜(1 << p)
        # check: mask & (1 << p) > 0
        def dfs(current, visited):
            if len(current) == k:
                print(current)
                return
            else:
                for i in range(n):
                    if not visited & (1 << i):
                        dfs(current + [i], visited |= (1 << i))
            