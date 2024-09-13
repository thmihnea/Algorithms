from typing import List

class Solution:
    def xor_array(self, arr: List[int], low: int, high: int):
        if low >= high:
            return arr[low]
        
        mid = (low + high) // 2
        return self.xor_array(arr, low, mid) ^ self.xor_array(arr, mid + 1, high)

    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        results: List[int] = []
        for query in queries:
            subarray: List[int] = arr[query[0]:query[1] + 1]
            results.append(self.xor_array(
                arr=subarray,
                low=0,
                high=len(subarray) - 1
            ))
        return results