class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def validate(node: TreeNode, 
                    min_val = float("-inf"), max_val = float("inf")) -> bool:

            # Handle the case if we reached a leaf.
            # This means we traversed the entire BST without any issues,
            # so we should return True.
            if node is None:
                return True

            # Check for definition corectness.
            if node.val <= min_val or node.val >= max_val:
                return False

            # We need to validate both left and right subtrees.
            return validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)

        return validate(root)
        