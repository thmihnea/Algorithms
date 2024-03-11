from typing import Dict

class Solution:
    def customSortString(self, order: str, s: str) -> str:

        """
        Setup the order table for our sorted string.
        We will use a pairing of the type (int, str) to
        keep track of which character should be on position i.
        """
        order_table: Dict[int, str] = dict()
        for i in range(len(order)):
            order_table[i] = order[i]

        """
        Create the table that holds all information
        regarding the string we wish to permute.
        """
        s_table: Dict[str, int] = dict()
        for char in s:
            s_table[char] = 1 if char not in s_table else s_table[char] + 1

        result: str = ""

        """
        Build the resultant string. We simply loop
        over each element in the order table, and we keep
        track of which element should be on position i. Then,
        on we add s_table[char] amount of char characters to the
        newly formed string.
        """
        for i in order_table:
            char: str = order_table[i]
            if char in s_table and s_table[char] > 0:
                result += (char * s_table[char])
                s_table[char] = 0

        # Add any remaining characters to the output.
        for char in s_table:
            result += (char * s_table[char])

        return result