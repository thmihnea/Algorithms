# A red-black tree is a way of implementing
# a 2-3 tree, where the red (left-leaning)
# link represents a middle link.
#
# In a 2-3 tree, we have perfect balance,
# i.e. the distance from the root to the
# leaves is the same regardless of path.
#
# To represent a 3-node in a 2-3 tree using a
# red-black tree, suppose we had 3-node with
# entries a and b, where a < b. Adding a red
# link between a and b, with a storing elements
# x < a to the left, and a < x < b to the right,
# and b storing a to the left (red link) and x > b
# to the right, we effectively create a BST.
#
# This means that every 2-3 tree has a corresponding
# red-black BST.
#
# Properties: no node has two red links connected to it,
# every path from root to leaves has the same number of
# black links, and red links lean left.
#
# Red-black trees have PERFECT BLACK BALANCE.

RED = True
BLACK = False

class Node(object):

    def __init__(self, key=None, value=None, left=None, right=None, color=RED):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.color = color

class RedBlackTree(object):

    def __init__(self):
        self.root = None
    
    def get(self, key):
        # The search method is identical to
        # regular BSTs.
        _current: Node = self.root
        while _current is not None:
            if key < _current.key:
                _current = _current.left
            elif key > _current.key:
                _current = _current.right
            elif key == _current.key:
                return _current.value
        return None
    
    def put(self, key, value):
        self.root = self._insert(self.root, key, value)
    
    def _insert(self, node: Node, key, value):
        if node is None:
            return Node(key=key, value=value, color=RED)
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        elif key == node.key:
            node.value = value
        
        if self.is_red(node.right) and not self.is_red(node.left):
            node = self._rotate_left(node)
        if self.is_red(node.left) and self.is_red(node.left.left):
            node = self._rotate_right(node)
        if self.is_red(node.left) and self.is_red(node.right):
            self._flip_color(node)

        return node
    
    def is_red(self, node: Node):
        if node is None:
            return False
        return node.color is RED
    
    def _rotate_left(self, h: Node):
        x: Node = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = RED
        return x
    
    def _rotate_right(self, h: Node):
        x: Node = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = RED
        return x
    
    def _flip_color(self, h: Node):
        h.color = RED
        h.left.color = BLACK
        h.right.color = BLACK

if __name__ == '__main__':
    rbt = RedBlackTree()
    s = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(s)):
        rbt.put(
            s[i],
            i + 1
        )
    print(rbt.get('f'))