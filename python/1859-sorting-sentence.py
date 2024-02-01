class Solution:

    def sortSentence(self, s: str) -> str:
        # Set up the data structures required for the problem.
        table: dict = dict()
        strings: list[str] = s.split()
        result: str = ""
        
        # Loop through the array, obtain the last character for each
        # string and set the table up accordingly.
        for entry in strings:
            last_char: str = entry[-1]
            i: int = int(last_char)
            table[i] = entry[0:-1]

        # Loop through the hashtable and append elements accordingly.
        # This approach gives us O(n) time complexity.
        for i in range(1, len(strings) + 1):
            result += table[i]
            if i != len(strings):
                result += " "

        return result

        