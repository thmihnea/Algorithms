class Node(object):

    def __init__(self, value, next):
        self.value = value
        self.next = next

class Stack(object):
    # Stack object implemented using a linked list.
    # This is faster because we do not have to use
    # array resizing, but it uses more memory.

    def __init__(self):
        self.first = None
    
    def empty(self):
        return self.first is None

    def push(self, value):
        _first = self.first
        _pushed = Node(
            value=value,
            next=_first
        )
        self.first = _pushed
    
    def pop(self):
        if self.first is None:
            return None
        _ret = self.first.value
        self.first = self.first.next
        return _ret