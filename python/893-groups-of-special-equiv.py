from typing import List
from collections import defaultdict

class Solution:
    def get_equivalent(self, word) -> str:
        even_table = defaultdict(int)
        odd_table = defaultdict(int)
        for i in range(0, len(word), 2):
            even_table[word[i]] += 1
        for i in range(1, len(word), 2):
            odd_table[word[i]] += 1
        result: str = ''
        even_table = sorted(list(even_table.items()))
        odd_table = sorted(list(odd_table.items()))
        for entry in even_table:
            result += f'{entry[0]}{entry[1]}'
        for entry in odd_table:
            result += f'{entry[0]}{entry[1]}'
        return result

    def numSpecialEquivGroups(self, words: List[str]) -> int:
        table = defaultdict(int)
        _max = float('-inf')
        for word in words:
            equivalent: str = self.get_equivalent(word)
            table[equivalent] += 1
            _max = max(_max, table[equivalent])
        return _max