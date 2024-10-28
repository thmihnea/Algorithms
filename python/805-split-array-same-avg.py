from typing import List

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        def dfs(i, j, current):
            if i == len(grid):
                return current

            if (i, j) in memo:
                return memo[(i, j)]
            
            value: int = grid[i][j]
            if j == 0:
                ret = dfs(i + 1, j + 1, current + value)
            elif j == len(grid[0]) - 1:
                ret = dfs(i + 1, j - 1, current + value)
            else:
                ret = min(
                    dfs(i + 1, j - 1, current + value),
                    dfs(i + 1, j + 1, current + value)
                )
            memo[(i, j)] = ret
            return ret
        
        ret = float('inf')
        for j in range(len(grid[0])):
            ret = min(ret, dfs(0, j, 0))
        return ret