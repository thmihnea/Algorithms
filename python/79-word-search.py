from typing import List, Dict, Tuple

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        We begin by setting up an array which will hold all
        possible traversal directions, i.e. UP, DOWN, LEFT, RIGHT.
        Also, we will use a global boolean variable (out of dfs function)
        that will be updated if the word exists.
        """
        directions: List[Tuple[int, int]] = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        found: bool = False

        def dfs(i: int, j: int, target: str, current: str, visited: Dict[Tuple[int, int], bool]):
            """
            The idea of the algorithm is to traverse to every possible
            neighbour of each point on the board. Then, we check if the index
            at which we are currently at, i.e. len(current), matches the letter, i.e.
            if board[i][j] == target[len(current)]. If this happens, we can then update
            the string we have found so far. 
            Afterwards, we simply check that we are within bounds and visit the next
            neighbour, making sure to mark the node as visited, and then popping it.
            """
            nonlocal found, directions
            coord: Tuple[int, int] = (i, j)
            if coord in visited:
                return
            
            result: str = "" if board[i][j] != target[len(current)] else current + board[i][j]
            if result == target:
                found = True
                return
            
            visited[coord] = True
            for entry in directions:
                new_coord: Tuple[int, int] = (i + entry[0], j + entry[1])
                if new_coord[0] < 0 or new_coord[0] >= len(board):
                    continue
                if new_coord[1] < 0 or new_coord[1] >= len(board[0]):
                    continue
                dfs(new_coord[0], new_coord[1], target, result, visited)
            visited.pop(coord)
        
        """
        It is not sufficient to simply start from (0, 0)
        on the board, as we need to visit every possible
        letter combination. For this reason, we visit from every
        pair (i, j).
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, word, "", {})

        """
        If any of the recursion chains above succeeded in finding
        the word, then it means found had to have been updated.
        Simply return found.
        """
        return found
        

        