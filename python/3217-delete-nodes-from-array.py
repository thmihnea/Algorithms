from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or len(nums) == 0:
            return head

        nums_set = set(nums)

        while head is not None and head.val in nums_set:
            head = head.next

        if head is None:
            return None

        _prev = head
        current = head.next

        while current is not None:
            if current.val in nums_set:
                _prev.next = current.next
            else:
                _prev = current
            current = current.next

        return head
