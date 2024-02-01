class ListNode:
    def __init__(self, val: int = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:

        # Convert linked-list into a list of integers utility function.
        def retrieve(head: ListNode) -> list[int]:
            solution: list[int] = []
            while head is not None:
                solution.append(head.val)
                head = head.next
            return solution

        # Append a list to another list utility function.
        def append(target: list[int], to_add: list[int]) -> None:
            for entry in to_add:
                target.append(entry)

        complete_list: list[int] = []

        # Decompose lists.
        for entry in lists:
            items: list[int] = retrieve(entry)
            append(complete_list, items)

        # Sort.
        complete_list.sort()

        if len(complete_list) == 0:
            return None

        # Reconstruct linked list.
        head: ListNode = ListNode(val = complete_list[0])
        current: ListNode = head
        index: int = 1

        while index < len(complete_list):
            new_node: ListNode = ListNode(val = complete_list[index])
            current.next = new_node
            current = new_node
            index += 1

        return head

        