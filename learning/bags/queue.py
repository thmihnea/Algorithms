class Node(object):

    def __init__(self, value, next):
        self.value = value
        self.next = next

class Queue(object):

    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0
    
    def empty(self):
        return self.first is None
    
    def size(self):
        return self._size

    def pop(self):
        # Remove item from front of queue.
        if self.first is None:
            return None
        _ret = self.first.value
        self.first = self.first.next
        self._size -= 1
        return _ret
    
    def push(self, value):
        # Push an item onto the queue.
        _last = self.last
        _node = Node(
            value=value,
            next=None
        )
        self.last = _node
        self._size += 1
        if self.first is None:
            self.first = self.last
        if _last is not None:
            _last.next = self.last