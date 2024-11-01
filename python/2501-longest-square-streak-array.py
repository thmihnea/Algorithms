from typing import List
from math import sqrt

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        table: dict[int, int] = {}
        result: int = -1

        for entry in nums:
            root: float = sqrt(entry)
            if root * root == entry and root in table:
                table[entry] = table[root] + 1
                result = max(result, table[entry])
            else:
                table[entry] = 1

        return result