from typing import List

class Solution:
    def search(self, low: int, high: int, left: bool) -> int:
        if low > high:
            return -1
        mid: int = low + (high - low) // 2
        if self.nums[mid] == self.target:
            if left:
                left_ocurrance: int = self.search(low, mid - 1, left)
                return left_ocurrance if left_ocurrance != -1 else mid
            else:
                right_ocurrance: int = self.search(mid + 1, high, left)
                return right_ocurrance if right_ocurrance != -1 else mid
        elif self.nums[mid] > self.target:
            return self.search(low, mid - 1, left)
        else:
            return self.search(mid + 1, high, left)

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.target = target
        left: int = self.search(0, len(nums) - 1, True)
        right: int = self.search(0, len(nums) - 1, False)
        return [left, right]