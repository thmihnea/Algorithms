class Solution:
    def maxDepth(self, s: str) -> int:
        """
        Initialize a counter and a maximum depth variable.
        The idea is to simply loop through the string until
        we reach a paranthesis. If it is "(", increment
        the counter by one; otherwise, decrement it. Make
        sure to update the counter when we increment the counter.
        """
        counter: int = 0
        max_depth: int = 0
        for char in s:
            if char == '(':
                counter += 1
                max_depth = max(counter, max_depth)
            elif char == ')':
                counter -= 1
        return max_depth

        