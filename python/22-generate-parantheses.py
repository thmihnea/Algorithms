from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # Helper function to check if any possible
        # combination is a valid solution.
        def is_valid(s: str) -> bool:
            count = 0
            for char in s:
                if char == "(":
                    count += 1
                elif char == ")":
                    if count <= 0:
                        return False
                    count -= 1
            return count == 0

        # Backtracking function for generating all
        # possible solutions.
        def backtrack(n: int, s: str, solution: List[str]):
            # If we reach the intended length, we check if
            # what we generated is a solution.
            if len(s) == n:
                if is_valid(s):
                    solution.append(s)
            # If we did not reach the length, we simply
            # continue by generating another solution.
            else:
                for char in ["(", ")"]:
                    backtrack(n, s + char, solution)

        # Prepare data structures and call the backtracking
        # function.
        solution: List[str] = []
        backtrack(2 * n, "", solution)

        return solution
