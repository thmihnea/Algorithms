from typing import List

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        result: List[int] = [0]
        idx: int = 0
        while len(result) < k:
            invert: List[int] = [entry ^ 1 for entry in result]
            result = result + [1] + invert[::-1]
            idx += 1
        return str(result[k - 1])
        