# A binary search tree is a binary tree in 
# symmetric order => left child is smaller,
# right child is greater than parent.
#
# We can use a BST to implement a symbol table
# if the keys are comparable.

class Node(object):

    def __init__(self, left=None, right=None, key=None, value=None):
        self.left = left
        self.right = right
        self.key = key
        self.value = value
        self.count = 0

class BinarySearchTree(object):

    def __init__(self, root=None):
        self.root = root

    def put(self, key, value):
        self.root = self._insert(self.root, key, value)

    def get(self, key):
        _node: Node = self._search(key)
        return None if _node is None else _node.value

    def _search(self, key) -> Node:
        _root: Node = self.root
        while _root is not None:
            if key == _root.key:
                return _root
            elif key < _root.key:
                _root = _root.left
            else:
                _root = _root.right
        return None

    def _insert(self, node: Node, key, value) -> Node:
        if node is None:
            return Node(
                key=key,
                value=value
            )
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            node.value = value
        node.count = 1 + self.size(node.left) + self.size(node.right)
        return node
    
    def size(node: Node) -> int:
        return 0 if node is None else node.count
    
if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.put('a', 1)
    tree.put('b', 2)
    tree.put('c', 3)
    print(tree.get('a'), tree.get('b'), tree.get('c'))