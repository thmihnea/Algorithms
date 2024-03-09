from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        i: int = 0
        j: int = 0

        while i < len(nums1) and j < len(nums2):
            # If the elements match, then we are done.
            if nums1[i] == nums2[j]:
                return nums1[i]
            
            # Because each array is sorted in increasing order,
            # if nums1[i] > nums2[j], we must increment j to obtain
            # an element closer to nums1[i].
            elif nums1[i] > nums2[j]:
                j += 1
            # Repeat the same logic if nums1[i] < nums2[j].
            else:
                i += 1
        
        # Return -1 if no solution was found.
        return -1
        