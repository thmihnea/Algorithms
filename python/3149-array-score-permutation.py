from typing import List

class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        self.nums: List[int] = nums
        self.length: int = len(nums)
        self.min_score: int = float('inf')
        self.permutation: List[int] = []

        def dfs(current, mask, current_score):
            if current_score >= self.min_score:
                return

            if len(current) == self.length:
                if current_score < self.min_score:
                    self.min_score = current_score
                    self.permutation = current[:]
            else:
                for i in range(self.length):
                    if not mask & (1 << i):
                        new_score = current_score
                        if len(current) > 0:
                            new_score += abs(current[-1] - self.nums[i])
                        if len(current) == self.length - 1:
                            new_score += abs(i - self.nums[current[0]])
                        dfs(current + [i], mask | (1 << i), new_score)

        dfs([], 0, 0)
        return self.permutation
