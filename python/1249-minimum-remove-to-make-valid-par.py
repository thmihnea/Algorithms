from typing import List, Dict

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack: List[int] = []
        invalid: Dict[int, bool] = dict()

        """
        Use a stack to keep track of which parantheses
        have not been closed. Also, if we are in an invalid state,
        i.e. a right paranthesis ")" is opened with len(stack) == 0,
        keep it in a dict.
        """
        def build() -> None:
            nonlocal stack, invalid, s
            for i in range(len(s)):
                char: str = s[i]
                if char == '(':
                    stack.append(i)
                elif char == ')':
                    if len(stack) == 0:
                        invalid[i] = True
                    else:
                        stack.pop()
        
        """
        Rebuild the validated string.
        """
        def construct() -> str:
            nonlocal stack, invalid, s
            for entry in stack:
                invalid[entry] = True
            new_str: str = ""
            for i in range(len(s)):
                char = s[i]
                if i not in invalid:
                    new_str += s[i]
            return new_str

        build()
        return construct()

        