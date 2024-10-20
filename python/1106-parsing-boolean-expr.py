from typing import List

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        expression_stack: List[str] = []
        for char in expression:
            if char == ',' or char == '(':
                continue
            if char in ['t', 'f', '!', '|', '&']:
                expression_stack.append(char)
            elif char == ')':
                found_true: bool = False
                found_false: bool = False
                while expression_stack[-1] not in ['!', '|', '&']:
                    top: str = expression_stack.pop()
                    if top == 'f':
                        found_false = True
                    elif top == 't':
                        found_true = True
                operation: str = expression_stack.pop()
                if operation == '!':
                    expression_stack.append('t' if not found_true else 'f')
                elif operation == '&':
                    expression_stack.append('t' if not found_false else 'f')
                else:
                    expression_stack.append('t' if found_true else 'f')
        return expression_stack[-1] == 't'