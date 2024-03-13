import math

class Solution:
    def pivotInteger(self, n: int) -> int:
        """
        The sum of integers from 1 to x is x * (x + 1) / 2. From x
        to n, it is n * (n + 1) / 2 - (x - 1) * x / 2. Equating both 
        sides yields x^2 = n * (n + 1) / 2. The solution to this equation
        is our result. If x is an integer, we simply return it.
        Otherwise, we return -1.
        """
        target: int = n * (n + 1) // 2
        x: int = math.isqrt(target)
        return x if x ** 2 == target else -1
        