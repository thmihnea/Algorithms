from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def is_inside(pos_i: int, pos_j: int):
            nonlocal grid
            return (pos_i >= 0 and pos_i < len(grid)) and (pos_j >= 0 and pos_j < len(grid[0]))

        def dfs(pos_i: int, pos_j: int):
            nonlocal grid, directions
            grid[pos_i][pos_j] = 0
            for direction in directions:
                new_i: int = pos_i + direction[0]
                new_j: int = pos_j + direction[1]
                if is_inside(new_i, new_j) and grid[new_i][new_j] == "1":
                    dfs(new_i, new_j)

        count: int = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        return count
        