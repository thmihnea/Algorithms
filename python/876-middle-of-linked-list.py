from typing import Optional

# Definition of a node in a linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Utility function to return the length of
        # a linked list by linear search.
        def length(node: Optional[ListNode]) -> int:
            if node is None:
                return 0
            return 1 + length(node.next)

        # Auxiliary function to return the n-th element
        # in a linked list.
        def get_node(node: Optional[ListNode], target: int) -> Optional[ListNode]:
            current: int = 1
            aux: ListNode = node
            while current < target:
                aux = aux.next
                current += 1
            return aux

        target: int = length(head) // 2 + 1
        return get_node(head, target)

        