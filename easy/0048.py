"""48. Rotate Image"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        for row in range((length := len(matrix)) // 2):
            for column in range(length):
                matrix[row][column], matrix[-row - 1][column] = (
                    matrix[-row - 1][column],
                    matrix[row][column],
                )

        for row in range(length):
            for column in range(row):
                matrix[row][column], matrix[column][row] = (
                    matrix[column][row],
                    matrix[row][column],
                )
