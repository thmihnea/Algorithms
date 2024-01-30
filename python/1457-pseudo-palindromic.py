class TreeNode:
    
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.counter = 0

    def isLeaf(self, node: TreeNode) -> bool:
        return node.left == None and node.right == None

    def isPalindrome(self, table: list[int]) -> bool:
        frequency_map: dict = dict()
        for element in table:
            frequency_map[element] = 1 if element not in frequency_map else frequency_map[element] + 1
        if len(frequency_map) == 1:
            return True
        odd_elements: int = 0
        for element in frequency_map:
            if frequency_map[element] % 2 == 1:
                odd_elements += 1
        return odd_elements <= 1

    def generatePaths(self, node: TreeNode, table: list[TreeNode]) -> None:
        table.append(node.val)

        if self.isLeaf(node):
            if self.isPalindrome(table):
                self.counter += 1
            table.pop()
        else:
            if node.left is not None:
                self.generatePaths(node.left, table)
            if node.right is not None:
                self.generatePaths(node.right, table)
            table.pop()

    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        table: list[TreeNode] = []
        self.generatePaths(root, table)

        return self.counter
        