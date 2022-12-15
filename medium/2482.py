"""2482. Difference Between Ones and Zeros in Row and Column"""

from typing import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        width = len(grid[0])
        height = len(grid)

        x_result = [2 * sum(row) - width for row in grid]
        y_result = [2 * sum(row[i] for row in grid) - height for i in range(width)]

        diff = [[0] * width for _ in range(height)]

        for i in range(height):
            for j in range(width):
                diff[i][j] = x_result[i] + y_result[j]

        return diff
