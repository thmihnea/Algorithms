from typing import List

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        # Simply use the sorted method to obtain the wanted result.
        return sorted(score, key = lambda item: item[k], reverse = True)