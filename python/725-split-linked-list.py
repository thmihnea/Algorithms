from typing import Optional, List, Any

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def _get_parts(self, n: int, k: int) -> List[int]:
        # Divides the number n into k (semi) equal parts.
        parts: List[int] = []
        base_part: int = n // k
        parts_left: int = n - base_part * k

        for _ in range(k):
            amount: int = base_part
            if parts_left > 0:
                amount += 1
                parts_left -= 1
            parts.append(amount)

        return parts
    
    def _length(self, head: Optional[ListNode]) -> int:
        # Returns the length of the linked list.
        if head is None:
            return 0

        length: int = 0
        while head is not None:
            length += 1
            head = head.next
        
        return length

    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Performs the splitting operation.
        parts: List[int] = self._get_parts(
            n=self._length(head),
            k=k
        )
        split_list: List[Optional[ListNode]] = []
        
        for i in range(len(parts)):
            if parts[i] == 0:
                split_list.append(None)
                continue
            amount: int = 0
            appended: bool = False
            while amount < parts[i]:
                if not appended:
                    split_list.append(head)

                appended = True
                amount += 1

                prev: Optional[ListNode] = head
                head = head.next
                if amount == parts[i]:
                    prev.next = None
        
        return split_list
