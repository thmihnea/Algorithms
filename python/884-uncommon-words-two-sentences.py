from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        table: dict[str, int] = {}
        result: List[str] = []

        for c in s1.split(' '):
            table[c] = 1 if c not in table else table[c] + 1
        for c in s2.split(' '):
            table[c] = 1 if c not in table else table[c] + 1

        for entry in table:
            if table[entry] == 1:
                result.append(entry)

        return result

