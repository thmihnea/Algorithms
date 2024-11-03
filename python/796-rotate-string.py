class Solution:
    def rotate_once(self, s: str) -> str:
        res: str = ''
        for i in range(1, len(s)):
            res += s[i]
        res += s[0]
        return res

    def rotateString(self, s: str, goal: str) -> bool:
        if s == goal:
            return True
        copy: str = self.rotate_once(s)
        while copy != s:
            if copy == goal:
                return True
            copy = self.rotate_once(copy)
        return False