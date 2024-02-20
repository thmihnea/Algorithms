class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        # Compute the sum of the numbers in the array, and
        # simply subtract it from n * (n + 1) / 2, which is
        # the sum of all numbers from 0 to n.
        return len(nums) * (len(nums) + 1) // 2 - sum(nums)
        