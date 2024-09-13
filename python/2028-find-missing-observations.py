from typing import List

class Solution:
    def _backtrack(self, required: int, solution: List[int], current: int = 0):
        if current == required:
            print(solution)
            return
        for i in range(1, 7):
            if current + i > required:
                break
            solution.append(i)
            self._backtrack(required, solution, current + i)
            solution.pop(i)

    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total_sum = mean * (n + len(rolls))
        rolls_sum = sum(rolls)
        sol = []
        self._backtrack(total_sum - rolls_sum, sol)