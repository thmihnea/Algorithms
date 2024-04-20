from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def is_inside(i: int, j: int) -> bool:
            nonlocal grid
            return (i >= 0 and i < len(grid)) and (j >= 0 and j < len(grid[0]))

        def get_contribution(i: int, j: int) -> int:
            nonlocal grid, directions
            contribution: int = 0
            for direction in directions:
                new_i: int = i + direction[0]
                new_j: int = j + direction[1]
                if not is_inside(new_i, new_j) or grid[new_i][new_j] == 0:
                    contribution += 1
            return contribution

        contribution: int = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] is not 0:
                    contribution += get_contribution(i, j)
        return contribution

        