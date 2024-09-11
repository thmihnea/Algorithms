from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # Check if array can be constructed.
        if m * n != len(original):
            return []
        
        # Initialize matrix.
        matrix = [[0 for _ in range(n)] for _ in range(m)]

        # Assign values per row.
        for i in range(m):
            matrix[i] = original[i * n : (i + 1) * n]
            
        return matrix