from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Safeguard statement. If head is null, return false.
        if head is None:
            return False

        # Prepare two pointers.
        first: ListNode = head
        second: ListNode = head.next

        # Let first -> first.next, and second -> second.next.next. This way,
        # the first pointer cycles through the list one step at a time,
        # while the second one cycles two steps at the time.
        # If they meet, there exists a cycle.
        while second is not None and second.next is not None:
            first = first.next
            second = second.next.next

            if first == second:
                return True
        
        return False
        