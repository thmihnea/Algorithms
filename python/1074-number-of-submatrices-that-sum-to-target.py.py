from typing import List
from collections import defaultdict

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m: int = len(matrix)
        n: int = len(matrix[0])
        
        # Initialize the count of submatrices that sum to target
        count = 0
        
        # Fix two rows, r1 and r2
        for r1 in range(m):
            # This array will store the cumulative sum between row r1 and r2 for each column
            col_sums = [0] * n
            
            for r2 in range(r1, m):
                # Use a hash map to count the cumulative sums for subarrays
                sums = defaultdict(int)
                sums[0] = 1  # Handles the case where a submatrix sum exactly matches the target
                
                cur_sum = 0
                
                # Iterate over the columns
                for col in range(n):
                    # Update the cumulative sum for the current column between rows r1 and r2
                    col_sums[col] += matrix[r2][col]
                    
                    # Calculate the current cumulative sum
                    cur_sum += col_sums[col]
                    
                    # Check if (cur_sum - target) exists in the hash map
                    if cur_sum - target in sums:
                        count += sums[cur_sum - target]
                    
                    # Add the current sum to the hash map
                    sums[cur_sum] += 1
        
        return count