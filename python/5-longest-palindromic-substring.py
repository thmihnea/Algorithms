class Solution:
    def longestPalindrome(self, s: str) -> str:

        def isPalindromic(s: str) -> bool:
            for i in range(len(s) // 2):
                if s[i] != s[len(s) - i - 1]:
                    return False
            return True

        if len(s) <= 1 or isPalindromic(s):
            return s

        current: str = ""
        max_length: int = -1

        for increment in range(1, len(s) + 1):
            for idx in range(len(s)):
                if idx + increment > len(s):
                    break
                substring: str = s[idx:idx + increment]
                if isPalindromic(substring):
                    length: int = increment + 1
                    current = substring if length > max_length else current
                    max_length = max(max_length, length)
        
        return current

        