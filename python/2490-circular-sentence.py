class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        chars = sentence.split(' ')
        if chars[-1][-1] != chars[0][0]:
            return False
        for i in range(len(chars) - 1):
            if chars[i][-1] != chars[i + 1][0]:
                return False
        return True