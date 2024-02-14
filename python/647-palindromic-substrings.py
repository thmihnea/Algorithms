class Solution:
    def countSubstrings(self, s: str) -> int:

        def isPalindromic(s: str) -> bool:
            """
            Utility function to check if a string is palindromic.
            This method is faster than reversing and comparing.
            """
            for i in range(len(s) // 2):
                if s[i] != s[len(s) - i - 1]:
                    return False
            return True

        # Initialize the counter with the length of the string as
        # each individual character can be considered a palindrome.
        counter: int = len(s)

        # Use an incremental way to loop over all possible
        # cases.
        for increment in range(2, len(s) + 1):
            for idx in range(len(s)):
                # If we go out of index (> len(s)), simply
                # break as there is no need to further increment the index.
                if idx + increment > len(s):
                    break
                # Generate the substring.
                substring: str = s[idx:idx + increment]
                if isPalindromic(substring):
                    counter += 1

        return counter
        