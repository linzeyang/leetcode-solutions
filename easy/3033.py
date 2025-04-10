"""3033. Modify the Matrix"""

from typing import List


class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        len_y = len(matrix[0])

        col_maxs = [max(row[col] for row in matrix) for col in range(len_y)]

        for row in matrix:
            for idx, num in enumerate(row):
                if num == -1:
                    row[idx] = col_maxs[idx]

        return matrix
