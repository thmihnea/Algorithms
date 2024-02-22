class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        # Handle the case where there is only one person
        # in the list.
        if n == 1:
            return 1

        # Generate hashtables accordingly.
        trusts: dict = dict()
        trusted_by: dict = dict()

        for entry in trust:
            a: int = entry[0]
            b: int = entry[1]

            if a not in trusts:
                trusts[a] = [b]
            else:
                trusts[a].append(b)

            if b not in trusted_by:
                trusted_by[b] = [a]
            else:
                trusted_by[b].append(a)

        # Obtain result.
        for i in range(1, n + 1):
            if i not in trusted_by:
                continue
            if len(trusted_by[i]) != n - 1:
                continue
            if i in trusts:
                continue
            return i

        return -1
        