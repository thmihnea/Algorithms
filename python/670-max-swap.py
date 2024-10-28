from typing import List

class Solution:
    def convert(self, num: int) -> List[int]:
        result: List[int] = []
        while num > 0:
            result.append(num % 10)
            num //= 10
        result.reverse()
        return result

    def maximumSwap(self, num: int) -> int:
        max_digit: int = 0
        max_i: int = 0
        swap_i, swap_j = -1
        num = self.convert(num)

        for i in reversed(range(len(num))):
            if num[i] > max_digit:
                max_digit = num[i]
                max_i = i
            if num[i] < max_digit:
                swap_i, swap_j = i, max_i
        num[swap_i], num[swap_j] = num[swap_j], num[swap_i]
        return int(''.join([str(x) for x in num]))