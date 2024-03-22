from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        def is_pal_str(x: str) -> bool:
            low: int = 0
            high: int = len(x) - 1

            while low < high:
                if x[low] != x[high]:
                    return False
                low += 1
                high -= 1
            
            return True
        
        def convert(head: Optional[ListNode]) -> str:
            value: str = ""
            while head is not None:
                value += str(head.val)
                head = head.next
            return value
        
        return is_pal_str(convert(head))
        