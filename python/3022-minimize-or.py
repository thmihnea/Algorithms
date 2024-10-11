from typing import List

class Solution:
    def minOrAfterOperations(self, nums: List[int], k: int) -> int:
        mask: int = 0
        for i in range(29, -1, -1):
            mask |= (1 << i)
            print(bin(mask))
