class Solution:
    def numSquares(self, n: int) -> int:

        def solve(x: int, table: dict) -> int:
            # Base case. If x is lower or equal to zero,
            # simply return 0.
            if x <= 0:
                return 0
            
            # If we have already memoized x in our
            # DP table, just return the value without
            # performing any further recursion.
            if x in table:
                return table[x]
            
            # Answer starts at base case (x = sum of 1^2).
            answer: int = x
            for i in range(1, x):
                # Prematurely stop to obtain O(nsqrt(n)).
                if i * i > x:
                    break
                else:
                    square: int = i * i
                    # The answer is the minimum value between itself and
                    # the steps it takes to solve for x - square, to which we
                    # add one (as we have already used square).
                    answer = min(answer, 1 + solve(x - square, table))
            
            # Memoize answer.
            table[x] = answer
            return answer
        
        # Prepare data structure and solve.
        table: dict = dict()
        return solve(n, table) 
