from typing import Optional, List
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        table = defaultdict(list)
        min_col = 0
        max_col = 0

        table[0].append((root.val, 0, 0))

        def dfs(node: Optional[TreeNode], current: tuple[int, int]):
            nonlocal min_col, max_col
            if node is None:
                return

            left = node.left
            right = node.right

            if left is not None:
                left_coord = (current[0] + 1, current[1] - 1)
                table[left_coord[1]].append((left.val, left_coord[0], left_coord[1]))
                min_col = min(min_col, left_coord[1])
                dfs(left, left_coord)
            if right is not None:
                right_coord = (current[0] + 1, current[1] + 1)
                table[right_coord[1]].append((right.val, right_coord[0], right_coord[1]))
                max_col = max(max_col, right_coord[1])
                dfs(right, right_coord)
            
        
        dfs(root, (0, 0))
        result: List[int] = []
        while min_col <= max_col:
            arr = sorted(
                table[min_col],
                key=lambda x: (x[1], x[0])
            )
            arr = [element[0] for element in arr]
            result.append(arr)
            min_col += 1
        return result