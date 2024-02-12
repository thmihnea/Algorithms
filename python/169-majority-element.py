class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # Very easy problem - just find the highest occuring element.

        table: dict = dict()
        for entry in nums:
            table[entry] = 1 if entry not in table else table[entry] + 1

        max_entries: int = -1
        max_value: int = -1

        for entry in table:
            if table[entry] >= max_entries:
                max_entries = table[entry]
                max_value = entry

        return max_value
        