from typing import List
from collections import defaultdict

class Solution:
    def dfs(self, current, mask):
        self.table[current].add(mask)
        if mask == (1 << (len(self.nums) + 1)) - 1:
            return
        else:
            for i in range(len(self.nums)):
                if mask & (1 << i):
                    continue
                self.dfs(current | self.nums[i], mask | (1 << i))

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        self.nums = nums
        self.table = defaultdict(set)
        self.dfs(0, 0)
        
        max_entry: int = max(self.table, key=lambda x: x)
        return len(self.table[max_entry])