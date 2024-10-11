from typing import List

class Solution:
    def distance(self, a: int, b: int):
        xor = a ^ b
        count = 0
        while xor > 0:
            count += xor & 1
            xor >>= 1
        return count
        
    def totalHammingDistance(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                total += self.distance(nums[i], nums[j])
        return total