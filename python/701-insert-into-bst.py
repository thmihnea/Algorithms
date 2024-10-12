from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insert(self, value: int):
        self.root = self._insert(node=self.root, value=value)

    def _insert(self, node: Optional[TreeNode], value: int) -> Optional[TreeNode]:
        if node is None:
            return TreeNode(val=value)

        if value < node.val:
            node.left = self._insert(node=node.left, value=value)
        else:
            node.right = self._insert(node=node.right, value=value)
        
        return node

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.root = root
        self.insert(val)
        return self.root