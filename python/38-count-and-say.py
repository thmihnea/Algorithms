from typing import Dict

class Solution:
    def countAndSay(self, n: int) -> str:
        # We use this dictionary to memoize all previous solutions.
        memo: Dict[int, str] = dict()
        
        def generate(n: int) -> str:
            nonlocal memo
            if n == 1:
                return "1"
            if n in memo:
                return memo[n]
            else:
                # Obtain the previous solution, initialize an index pointer and
                # the resulting string which we will now generate.
                previous: str = generate(n - 1)
                idx: int = 0
                result: str = ""

                """
                The idea here is to initialize the index and simply
                move it to the right as long as we are constantly reading
                the same character. Once we no longer read the same character,
                we can just update our result and increase the pointer accordingly.
                Note that this operation is actually O(n) although we
                use two while loops.
                """
                while idx < len(previous):
                    counter: int = 0
                    char: str = previous[idx]

                    while idx + counter < len(previous) and previous[idx + counter] == char:
                        counter += 1
                    
                    result += str(counter)
                    result += char
                    idx += counter

                # Store the result in the table and return it.
                memo[n] = result
                return result
        
        return generate(n)
        