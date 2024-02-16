class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        table: dict = dict()

        for entry in arr:
            table[entry] = 1 if entry not in table else table[entry] + 1

        table = dict(sorted(table.items(), key = lambda item: item[1]))
        
        for entry in table:
            if k == 0:
                break

            minimum: int = min(table[entry], k)
            k -= minimum

            table[entry] -= minimum

        count: int = 0

        for entry in table:
            if table[entry] != 0:
                count += 1

        return count

        