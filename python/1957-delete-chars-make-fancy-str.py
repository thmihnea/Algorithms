class Solution:
    def makeFancyString(self, s: str) -> str:
        result: str = ''
        previous_char: str = ''
        char_count: int = 0

        for char in s:
            if previous_char != char:
                result += char
                char_count = 1
                previous_char = char
            else:
                if char_count < 2:
                    result += char
                    char_count += 1
        
        return result