from typing import List, Dict

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        table: Dict[int, bool] = dict()
        for entry in nums:
            table[entry] = True
        max_value: int = -1
        for entry in table:
            if entry > 0 and -entry in table:
                max_value = max(max_value, entry)
        return max_value