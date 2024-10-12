from typing import List

class Solution:
    def intersects(self, first: List[int], second: List[int]) -> bool:
        return first[0] <= second[1] and first[1] >= second[0]


    def minGroups(self, intervals: List[List[int]]) -> int:
        start: List[int] = [entry[0] for entry in intervals]
        end: List[int] = [entry[1] for entry in intervals]
        
        start.sort()
        end.sort()

        i: int = 0
        j: int = 0
        result: int = 0

        while i < len(intervals):
            if start[i] <= end[j]:
                i += 1
            else:
                j += 1
            result = max(result, i - j)
        return result