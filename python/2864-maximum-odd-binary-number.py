from typing import Dict

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        table: Dict[str, int] = {
            "0": 0,
            "1": 0
        }

        for char in s:
            table[char] += 1

        ones_size: int = table["1"]
        zeros_size: int = table["0"]
        result: str = ""

        if ones_size > 1:
            for _ in range(ones_size - 1):
                result += "1"
        if zeros_size > 0:
            for _ in range(zeros_size):
                result += "0"
        result += "1"

        return result
        