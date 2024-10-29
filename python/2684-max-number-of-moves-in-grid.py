from typing import List

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        memo = {}
        def dfs(i, j):
            if not (0 <= i < len(grid)):
                return 0
            if not (0 <= j < len(grid[0])):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            move_up, move_right, move_down = -1, -1, -1

            if 0 <= i - 1 < len(grid) and j + 1 < len(grid[0]):
                move_up = dfs(i - 1, j + 1) if grid[i][j] < grid[i - 1][j + 1] else -1
            if j + 1 < len(grid[0]):
                move_right = dfs(i, j + 1) if grid[i][j] < grid[i][j + 1] else -1
            if 0 <= i + 1 < len(grid) and j + 1 < len(grid[0]):
                move_down = dfs(i + 1, j + 1) if grid[i][j] < grid[i + 1][j + 1] else -1
            
            ret_value = 1 + max(move_up, move_right, move_down)
            memo[(i, j)] = ret_value

            return ret_value
        
        m = -1
        for i in range(len(grid)):
            m = max(dfs(i, 0), m)
        return m