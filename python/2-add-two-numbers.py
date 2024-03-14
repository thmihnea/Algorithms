from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        """
        This is a helper function that converts a linked
        list into a list of integers. Note that we also reverse
        the result because our data is pre-reversed.
        """
        def toArray(node: Optional[ListNode]) -> List[int]:
            nums: List[int] = []
            while node is not None:
                nums.append(node.val)
                node = node.next
            return list(reversed(nums))
        
        """
        Helper function that converts a number into a 
        linked list by its digits. Note the check for
        number > 0 inside the for loop - this is added
        as to ensure that we do not have an extra node
        when the number reaches nil.
        """
        def toLinkedList(number: int) -> Optional[ListNode]:
            head: ListNode = ListNode()
            last: ListNode = head
            while number > 0:
                digit: int = number % 10
                number = number // 10
                last.val = digit
                if number > 0:
                    new_node: ListNode = ListNode()
                    last.next = new_node
                    last = new_node
            return head
        
        """
        Helper function that converts a list of
        integers to a number.
        """
        def toNumber(nums: List[int]) -> int:
            result: int = 0
            for entry in nums:
                result *= 10
                result += entry
            return result
        
        # Prepare data, perform the summation.
        first: int = toNumber(toArray(l1))
        second: int = toNumber(toArray(l2))
        summation: int = first + second

        # Return the result.
        return toLinkedList(summation)