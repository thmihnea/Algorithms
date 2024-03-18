from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0

        points = sorted(points, key = lambda item: item[0])
        arrows: int = 1
        max_popped = points[0][1]

        for entry in points[1:]:
            if entry[0] > max_popped:
                arrows += 1
                max_popped = entry[1]
            else:
                max_popped = min(max_popped, entry[1])

        return arrows
        