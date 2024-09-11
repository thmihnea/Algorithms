from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def _to_list(self, head: Optional[ListNode]) -> List[int]:
        if head is None:
            return []
        
        _list: List[int] = []
        while head is not None:
            _list.append(head.val)
            head = head.next
        
        return _list

    def _exists_path(self, path: List[int], node: Optional[TreeNode], found: int = 0) -> bool:
        if node is None:
            return False
        
        _found: int = found
        
        
        if path[found] == node.val:
            _found += 1
        
        if _found == found:
            _found = 0
        
        if _found == len(path):
            return True
        
        return self._exists_path(path, node.left, _found) or self._exists_path(path, node.right, _found)

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        _list: List[int] = self._to_list(head)
        
        
        def dfs(node: Optional[TreeNode]) -> bool:
            if node is None:
                return False
            
            if self._exists_path(_list, node):
                return True
            
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)
