from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []
        if not nums1 or not nums2 or not k:
            return result
        
        heap = []
        visited = set()

        heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))
        visited.add((0, 0))

        while k and heap:
            _, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            
            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                visited.add((i + 1, j))
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
            
            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                visited.add((i, j + 1))
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

            k -= 1
        
        return result