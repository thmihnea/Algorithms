from typing import List

class Solution:
    def get_start(self, grid: List[List[int]]):
        m: int = len(grid)
        n: int = len(grid[0])
        start: tuple[int, int] = None
        count: int = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count += 1
                elif grid[i][j] == 1:
                    start = (i, j)
        
        return start, count

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m: int = len(grid)
        n: int = len(grid[0])

        start: tuple[int, int] = self.get_start(grid)
        coords: List[tuple[int, int]] = [
            (-1, 0), (0, 1), (1, 0), (0, -1)
        ]

        def dfs(path, visited):
            position = path[-1]
            if grid[position[0]][position[1]] == 2:
                print(path)
                return
            else:
                for coord in coords:
                    _i = position[0] + coord[0]
                    _j = position[1] + coord[1]
                    if (_i, _j) not in visited:
                        visited.add((_i, _j))
                        path.add((_i, _j))
                        dfs(path, visited)
                        path.pop()
                        visited.remove((_i, _j))
        
        path = [start]
        visited = set()
        visited.add(start)
        dfs(path, visited)