from typing import List, Dict

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # Initialize data structures.
        length: int = 0
        table: Dict[int, int] = {}
        left: int = 0

        """
        The idea is to use a sliding window approach and simply
        loop using the right pointer until we first reach an
        element with frequency > k. When that happens, move
        the left pointer until we no longer have a frequency of k.
        Update the result accordingly.
        """
        for right in range(len(nums)):
            table[nums[right]] = table.get(nums[right], 0) + 1
            if table[nums[right]] > k:
                while nums[left] != nums[right]:
                    table[nums[left]] -= 1
                    left += 1
                table[nums[left]] -= 1
                left += 1
            length = max(length, right - left + 1)
        return length