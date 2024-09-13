# A binary heap is an array representation of a
# heap-ordered complete binary tree.
#
# Heap-ordering -> parent's key is not
# smaller than the children's key.
# (Parent is always larger)
# 
# array[1] is the largest key. Also,
# the children of k are at 2k and 2k + 1.
# Hence, the parent of node k is k // 2.
#
# If child key becomes larger than parent key,
# we promote the child by exchanging arr[k] with arr[k // 2]
# recursively until parent is larger than both children.
# This is called the swim() method.
#
# If parent becomes smaller than children, figure out
# which child is bigger and perform recursive exchange with
# k and 2k OR 2k + 1.
# This is called the sink() method.
#
# Maximum element is at array[1]. To delete it, exchange
# element at the end of the heap with array[1] and remove it from
# the end, then sink it down to its level of competence.

from typing import List

class BinaryHeap(object):

    def __init__(self, capacity: int):
        self.heap: List[int] = [None for _ in range(capacity + 1)]
        self.size = 0
    
    def empty(self) -> bool:
        return self.size == 0
    
    def length(self) -> int:
        return self.size
    
    def insert(self, value: int):
        # Insert value at the end and
        # swim it up accordingly.
        self.size += 1
        self.heap[self.size] = value
        self._swim(value)
    
    def pop(self) -> int:
        # Pops (deletes) the maximum value.
        # Promotes the last element to root
        # and sinks it down accordingly.
        _max = self.heap[1]
        self._swap(1, self.size)
        self.heap[self.size] = None
        self.size -= 1
        self._sink(1)
        return _max
    
    def _swim(self, node: int):
        # Moves up a node until it is smaller than its parent.
        while node > 1 and self.heap[node] > self.heap[node // 2]:
            self._swap(node, node // 2)
            node = node // 2

    def _sink(self, node: int):
        while 2 * node <= self.size:
            j: int = 2 * node
            if self.heap[j + 1] is not None and self.heap[j] > self.heap[j + 1]:
                j = j + 1
            if not self.heap[node] < self.heap[j]:
                break
            self._swap(node, j)
            node = j

    def _swap(self, i: int, j: int):
        _temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = _temp

if __name__ == '__main__':
    heap = BinaryHeap(10)
    print(heap.empty())
    heap.insert(1)
    heap.insert(-1)
    heap.insert(3)
    heap.insert(2)
    print(heap.heap)
    while not heap.empty():
        print(heap.pop()) # Output 3->2->1->-1.