from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result: List[int] = []
        for i in range(len(nums)):
            entry: int = abs(nums[i])
            if nums[entry - 1] < 0:
                result.append(entry)
            nums[entry - 1] *= -1
        return result
        