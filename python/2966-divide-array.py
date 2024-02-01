class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        # Handle the case where the length of the list is
        # not divisible by three without allocating extra memory.
        if len(nums) % 3 != 0:
            return []

        # Prepare the solution array and sort the
        # initial list in ascending order.
        solution: list[list[int]] = []
        nums.sort()

        # Extract solution.
        for i in range(0, len(nums), 3):
            first: int = nums[i]
            second: int = nums[i + 1]
            third: int = nums[i + 2]
            if abs(first - second) <= k and abs(second - third) <= k and abs(first - third) <= k:
                solution.append([first, second, third])
            else:
                return []

        return solution
        