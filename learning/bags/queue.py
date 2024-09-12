class Node(object):

    def __init__(self, value, next):
        self.value = value
        self.next = next

class Queue(object):

    def __init__(self):
        self.first = None
        self.last = None
    
    def empty(self):
        return self.first is None

    def pop(self):
        # Remove item from front of queue.
        if self.first is None:
            return None
        _ret = self.first.value
        self.first = self.first.next
        return _ret
    
    def push(self, value):
        # Push an item onto the queue.
        _last = self.last
        _node = Node(
            value=value,
            next=None
        )
        self.last = _node
        if self.first is None:
            self.first = self.last
        if _last is not None:
            _last.next = self.last