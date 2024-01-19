"""73. Set Matrix Zeroes"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows: set[int] = set()
        cols: set[int] = set()

        for idx, row in enumerate(matrix):
            for jdx, num in enumerate(row):
                if not num:
                    rows.add(idx)
                    cols.add(jdx)

        for row in rows:
            for col in range(len(matrix[0])):
                if matrix[row][col]:
                    matrix[row][col] = 0

        for col in cols:
            for row in range(len(matrix)):
                if matrix[row][col]:
                    matrix[row][col] = 0
