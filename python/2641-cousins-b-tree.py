from typing import List, Optional
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __eq__(self, other):
        if isinstance(other, TreeNode):
            return (self.val == other.val and
                    self.left == other.left and
                    self.right == other.right)
        return False

    def __hash__(self):
        return hash((self.val, self.left, self.right))


class Solution:
    def dfs(self, node: Optional[TreeNode], level: int):
        if node is None:
            return

        self.table[level].append(node)
        
        if node.left is not None:
            self.parent[node.left] = node
            self.dfs(node.left, level + 1)
        
        if node.right is not None:
            self.parent[node.right] = node
            self.dfs(node.right, level + 1)
        

    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.table: dict[int, List[TreeNode]] = defaultdict(list)
        self.parent: dict[TreeNode, TreeNode] = {}

        self.dfs(root, 0)
        self.cousins: dict[TreeNode, List[TreeNode]] = defaultdict(list)

        for level in self.table:
            for node in self.table[level]:
                for other_node in self.table[level]:
                    if self.parent[node] != self.parent[other_node]:
                        self.cousins[node].append(other_node)

        print(self.cousins)
