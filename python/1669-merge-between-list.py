from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Initialize required variables.
        counter: int = 0
        previous_node: Optional[ListNode] = None
        current_node: Optional[ListNode] = list1

        # Helper function to get the last element of a linked list.
        def getLast(head: Optional[ListNode]) -> Optional[ListNode]:
            if head is None:
                return None
            if head.next is None:
                return head
            while head.next is not None:
                head = head.next
            return head

        # Remove elements from a to b.
        while counter <= b:
            if counter >= a:
                previous_node.next = current_node.next
                current_node = current_node.next
            else:
                if current_node.next is None:
                    break
                previous_node = current_node
                current_node = current_node.next
            counter += 1
        
        # Insert the other linked list.
        previous_node.next = list2
        getLast(list2).next = current_node

        return list1

        