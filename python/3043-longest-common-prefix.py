from typing import List

class TrieNode:
    def __init__(self, char, left=None, mid=None, right=None, marked=False):
        self.left = left
        self.mid = mid
        self.right = right
        self.char = char
        self.marked = marked

class TernaryTrie:
    def __init__(self):
        self.root: TrieNode = None

    def put(self, string):
        self.root = self._put(self.root, string, 0)
    
    def get(self, string) -> TrieNode:
        return self._get(self.root, string, 0)
    
    def contains(self, string) -> bool:
        node = self.get(string)
        return node is not None and node.marked
    
    def longest_prefix(self, string: str) -> int:
        return self._search(self.root, string, 0, 0)
    
    def _put(self, node: TrieNode, string: str, d: int) -> TrieNode:
        char = string[d]
        if node is None:
            node = TrieNode(char=char)
        
        if char < node.char:
            node.left = self._put(node.left, string, d)
        elif char > node.char:
            node.right = self._put(node.right, string, d)
        elif d < len(string) - 1:
            node.mid = self._put(node.mid, string, d + 1)
        else:
            node.marked = True
        
        return node

    def _get(self, node: TrieNode, string: str, d: int) -> TrieNode:
        if node is None:
            return None
        
        char = string[d]

        if char < node.char:
            return self._get(node.left, string, d)
        elif char > node.char:
            return self._get(node.right, string, d)
        elif d < len(string) - 1:
            return self._get(node.mid, string, d + 1)
        else:
            return node

    def _search(self, node: TrieNode, string: str, d: int, length: int) -> int:
        if node is None:
            return length
        if d >= len(string):
            return length
        
        char = string[d]
        
        if char < node.char:
            return self._search(node.left, string, d, length)
        elif char > node.char:
            return self._search(node.right, string, d, length)
        else:
            new_length = d + 1
            if new_length > length:
                length = new_length
            return self._search(node.mid, string, d + 1, length)

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1 = [str(entry) for entry in arr1]
        arr2 = [str(entry) for entry in arr2]

        trie = TernaryTrie()
        for entry in arr1:
            trie.put(entry)

        length: int = 0
        for entry in arr2:
            prefix_length = trie.longest_prefix(entry)
            if prefix_length > length:
                length = prefix_length
        
        return length