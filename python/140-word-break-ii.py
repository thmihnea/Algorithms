from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        solution: List[str] = []
        
        def dfs(idx, current, last):
            if idx == len(s):
                if len(last) > 0 and last in wordDict:
                    current = f'{current} {last}' if current else last
                    solution.append(current)
                return
            
            if last in wordDict:
                dfs(idx + 1, f'{current} {last}' if current else last, s[idx])
            dfs(idx + 1, current, last + s[idx])
        
        dfs(0, '', '')
        return solution