class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        If the length of s is zero, then simply
        return true, because the empty set is always
        a subset of any set.
        """
        if len(s) == 0:
            return True
        
        """
        Initialize an index and reconstruct the string
        in order. At the end of it, simply compare
        the two strings and check whether they are equal.
        """
        index: int = 0
        constructed_string: str = ""
        for char in t:
            if index >= len(s):
                break
            if char == s[index]:
                constructed_string += char
                index += 1
        return constructed_string == s
