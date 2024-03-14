from typing import List, Dict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int):
        count: Dict[int, int] = {0: 1}
        curr_sum: int = 0
        total_subarrays: int = 0
        
        for num in nums:
            curr_sum += num
            if curr_sum - goal in count:
                total_subarrays += count[curr_sum - goal]
            count[curr_sum] = count.get(curr_sum, 0) + 1

        return total_subarrays