from typing import List
import heapq
import math

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap: List[int] = []
        for entry in nums:
            heapq.heappush(heap, -entry)

        score: int = 0
        for _ in range(k):
            element: int = heapq.heappop(heap)
            score += (-element)
            element = -math.ceil(-element / 3)
            heapq.heappush(heap, element)

        return score