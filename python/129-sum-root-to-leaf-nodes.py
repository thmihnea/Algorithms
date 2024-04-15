from typing import Optional, List, Dict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(node: Optional[TreeNode], current: str):
            if node is None:
                return
            nonlocal visited, solutions
            if node in visited:
                return
            if node.left is None and node.right is None:
                solutions.append(int(current))
            else:
                if node.left is not None:
                    dfs(node.left, current + str(node.left.val))
                if node.right is not None:
                    dfs(node.right, current + str(node.right.val))
        
        visited: Dict[TreeNode, bool] = dict()
        solutions: List[str] = []

        dfs(root, str(root.val))

        return sum(solutions)
