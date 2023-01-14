"""766. Toeplitz Matrix"""

from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])

        if rows == 1 or columns == 1:
            return True

        for i in range(rows - 1):
            target = matrix[i][0]

            for j in range(1, min(rows - i, columns)):
                if matrix[i + j][j] != target:
                    return False

        for i in range(1, columns - 1):
            target = matrix[0][i]

            for j in range(1, min(rows, columns - i)):
                if matrix[j][i + j] != target:
                    return False

        return True
