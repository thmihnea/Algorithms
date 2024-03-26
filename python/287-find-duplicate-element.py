from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        previous: int = -1
        for entry in nums:
            if entry == previous:
                return entry
            previous = entry
        return -1

        