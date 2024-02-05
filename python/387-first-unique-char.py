class Solution:
    
    def firstUniqChar(self, s: str) -> int:
        
        def frequency(s: str):
            table: dict = dict()
            indices: dict = dict()

            for i in range(len(s)):
                char: str = s[i]
                if char == " ":
                    continue
                if char not in indices:
                    indices[char] = i
                table[char] = 1 if char not in table else table[char] + 1

            return table, indices

        freq, index = frequency(s)

        i: int = 10 ** 6
        found: bool = False

        for char in freq:
            appearences = freq[char]
            if appearences == 1:
                found = True
                j = index[char]
                i = j if i > j else i

        return i if found else -1