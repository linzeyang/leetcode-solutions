"""3212. Count Submatrices With Equal Frequency of X and Y"""

from typing import List


class Solution:
    """
    https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/
    Weekly Contest 405
    """

    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        cols: int = len(grid[0])
        x_sub: list[int] = [0] * cols
        y_sub: list[int] = [0] * cols

        out: int = 0

        for row in grid:
            curr_x: int = 0
            curr_y: int = 0

            for idx, cell in enumerate(row):
                if cell == "X":
                    curr_x += 1
                elif cell == "Y":
                    curr_y += 1

                x_sub[idx] += curr_x
                y_sub[idx] += curr_y

                if x_sub[idx] and x_sub[idx] == y_sub[idx]:
                    out += 1

        return out
