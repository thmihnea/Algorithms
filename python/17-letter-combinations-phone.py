from typing import List, Dict

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Handle the case when we pass the empty string or null.
        if not digits:
            return []

        # Mapping keeping track of all possible combinations of characters.
        number_mapping: Dict[int, List[str]] = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }

        # Backtracking function - simply permute all possible outcomes.
        def permute(digits: str, index: int, output: str, results: List[str]):
            if index == len(digits):
                results.append(output)
                return
            current_digit = int(digits[index])
            for letter in number_mapping[current_digit]:
                permute(digits, index + 1, output + letter, results)

        # Prepare the resultant array, and call the permute function.
        results = []
        permute(digits, 0, "", results)
        return results