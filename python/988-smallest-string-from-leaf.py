from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def smaller(s1: str, s2: str) -> str:
            # Compare strings lexicographically
            if s1 < s2:
                return s1
            else:
                return s2
        
        def dfs(node: Optional[TreeNode], current_str: str):
            nonlocal result
            if node is None:
                return
            current_str = chr(node.val + ord('a')) + current_str
            if node.left is None and node.right is None:  # Leaf node
                result = smaller(result, current_str)
                return
            dfs(node.left, current_str)
            dfs(node.right, current_str)

        result: str = "z" * (10 ** 4)  # Initialize with a large string
        dfs(root, '')
        return result