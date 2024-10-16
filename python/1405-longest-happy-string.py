from typing import List
import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result: str = ''
        heap: List[tuple[int, str]] = []

        for count, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if count != 0:
                heapq.heappush(heap, (count, char))

        while heap:
            count, char = heapq.heappop(heap)
            if len(result) > 1 and result[-1] == result[-2] == char:
                if not heap:
                    break
                _count, _char = heapq.heappop(heap)
                result += _char
                _count += 1
                if _count:
                    heapq.heappush(heap, (_count, _char))
            else:
                result += char
                count += 1
            if count:
                heapq.heappush(heap, (count, char))
        
        return result