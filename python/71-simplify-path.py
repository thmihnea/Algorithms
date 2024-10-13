from typing import List

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack: List[str] = []
        current: str = ''
        for i in range(len(path)):
            if path[i] != '/':
                current += path[i]
            else:
                if len(current) > 0:
                    stack.append(current)
                    current = ''
                continue
        if len(current) > 0:
            stack.append(current)
        path_stack: List[str] = []
        for entry in stack:
            if entry == '.':
                continue
            elif entry == '..':
                if len(path_stack) == 0:
                    continue
                else:
                    path_stack.pop()
            else:
                path_stack.append(entry)
        result: str = '/'
        for i in range(len(path_stack)):
            if i != len(path_stack) - 1:
                result += f'{path_stack[i]}/'
            else:
                result += path_stack[i]
        return result