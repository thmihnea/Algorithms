class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        def frequency(s: str) -> str:
            """
            This function returns the frequency signature of
            a string. Because we want to use a dictionary in order
            to group anagrams together, we need to have a hashable data
            structure for our dictionary keys - thus, we utilize a string.
            """
            table: dict = dict()

            # Build frequency table.
            for char in s:
                table[char] = 1 if char not in table else table[char] + 1

            # Sort the characters lexicographically and merge them into tuples
            # of the type (char, int) which hold a character and its number of
            # appearences.
            result: list = sorted(table.items(), key = lambda i: i[0])
            freq: str = ""

            # Build the frequency signature.
            for entry in result:
                freq += entry[0]
                freq += str(entry[1])

            return freq

        # Initialize required data structures.
        table: dict = dict()
        result: list = []

        # Build the frequency signature for each string. If our table
        # does not contain that signature, simply add a new key to the 
        # dictionary and remember all further strings which feature the same
        # signature.
        for entry in strs:
            freq = frequency(entry)
            if freq in table:
                table[freq].append(entry)
            else:
                table[freq] = [entry]

        # Group everything together.
        for entry in table:
            grouping: list = table[entry]
            result.append(grouping)

        return result

        