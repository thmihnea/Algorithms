from typing import List

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        _max = 0
        for j in range(len(nums2)):
            for i in range(len(nums1)):
                if nums1[i] != nums2[j]:
                    continue
                else:
                    k: int = 1
                    while i + k < len(nums1) and j + k < len(nums2) and nums1[i + k] == nums2[j + k]:
                        k += 1
                    _max = max(_max, k)
                    i = i + k
        return _max