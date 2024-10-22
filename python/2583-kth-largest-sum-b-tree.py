from collections import defaultdict
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, node: Optional[TreeNode], level: int):
        if node is None:
            return
        
        self.table[level].append(node.val)

        self.dfs(node.left, level + 1)
        self.dfs(node.right, level + 1)

    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        self.table = defaultdict(list)
        self.dfs(root, 0)

        if len(self.table) < k:
            return -1
        
        sums: List[int] = sorted([sum(self.table[entry]) for entry in self.table], reverse=True)
        return sums[k - 1]
        