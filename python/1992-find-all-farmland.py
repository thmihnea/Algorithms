from typing import List, Tuple

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        # Define the directions to check adjacent cells
        directions: List[Tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Check if coordinates are inside the land grid
        def is_inside(i: int, j: int) -> bool:
            return 0 <= i < len(land) and 0 <= j < len(land[0])

        # Recursive function to find the top-left corner of farmland
        def find_top_left(i: int, j: int):
            if is_inside(i - 1, j) and land[i - 1][j] == 1:
                return find_top_left(i - 1, j)
            elif is_inside(i, j - 1) and land[i][j - 1] == 1:
                return find_top_left(i, j - 1)
            elif land[i][j] == 1:
                return (i, j)
            else:
                return None

        # Recursive function to find the bottom-right corner of farmland
        def find_bot_right(i: int, j: int):
            if is_inside(i + 1, j) and land[i + 1][j] == 1:
                return find_bot_right(i + 1, j)
            elif is_inside(i, j + 1) and land[i][j + 1] == 1:
                return find_bot_right(i, j + 1)
            elif land[i][j] == 1:
                return (i, j)
            else:
                return None

        # Function to mark farmland as visited
        def clear(i: int, j: int):
            land[i][j] = 0
            for direction in directions:
                new_i, new_j = i + direction[0], j + direction[1]
                if is_inside(new_i, new_j) and land[new_i][new_j] == 1:
                    clear(new_i, new_j)

        results: List[List[int]] = []

        # Iterate through each cell in the land grid
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] == 1:  # If cell contains farmland
                    # Find the top-left and bottom-right corners of farmland
                    top_left: Tuple[int, int] = find_top_left(i, j)
                    bot_right: Tuple[int, int] = find_bot_right(i, j)
                    if top_left and bot_right:  # If both corners are found
                        # Store the coordinates of farmland
                        res: List[int] = [top_left[0], top_left[1], bot_right[0], bot_right[1]]
                        results.append(res)
                        clear(i, j)  # Clear the farmland area

        return results
