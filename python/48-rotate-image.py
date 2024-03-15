from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Retrieve the size of the matrix.
        n: int = len(matrix)
        """
        The idea of this problem is to first compute the
        transpose of the matrix. After computing the transpose,
        in order to complete the problem, we must also reverse
        each row in the matrix.
        """
        for i in range(n):
            for j in range(i):
                aux: int = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = aux
        # Reverse each row of the matrix. We fully rotated the image.     
        for i in range(n):
            matrix[i] = reversed(matrix[i])
        