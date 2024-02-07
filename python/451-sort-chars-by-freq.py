class Solution:
    def frequencySort(self, s: str) -> str:
        
        # Construct the table which holds frequency-related data
        # for our string.
        table: dict = dict()
        for char in s:
            table[char] = 1 if char not in table else table[char] + 1

        # Sort the table in reverse. This operation makes our total complexity
        # be O(nlogn).    
        table = sorted(table.items(), reverse = True, key = lambda i: i[1])

        # Build the resultant string. Note that even though there
        # are two for loops, we have a total of n operations being done.
        # This does not affect our complexity.
        result: str = ""
        for entry in table:
            count = entry[1]
            for _ in range(count):
                result += entry[0]

        return result