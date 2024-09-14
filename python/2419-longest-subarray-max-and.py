from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_value: int = max(nums)
        idx: int = 0
        current_length: int = 0
        max_length: int = 0

        while idx < len(nums):
            if nums[idx] == max_value:
                current_length += 1
            else:
                max_length = max(max_length, current_length)
                current_length = 0
            idx += 1
        return max(current_length, max_length)