class Solution:
    def minimumLength(self, s: str) -> int:

        # Initialize a left and right pointer.
        left: int = 0
        right: int = len(s) - 1

        # As long as they intersect and they are equal, we can 
        # proceed and do the required adjustments.
        while left < right and s[left] == s[right]:
            # Get the current character.
            char: str = s[left]
            # As long as they do not intersect, and as long as
            # the left side is on the same character, move the
            # left pointer to the right by one.
            while left <= right and s[left] == char:
                left += 1
            # As long as they do not intersect, and as long as
            # the right side is on the same character, move the
            # right pointer to the left by one.
            while right >= left and s[right] == char:
                right -= 1

        # When there are no more valid prefixes/suffixes, simply
        # return the length of the interval [left, right].
        return right - left + 1
        