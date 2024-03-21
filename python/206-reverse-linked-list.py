from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous: Optional[ListNode] = None
        current: Optional[ListNode] = head

        while current is not None:
            next_node: Optional[ListNode] = current.next
            current.next = previous
            previous = current
            current = next_node

        return previous
        