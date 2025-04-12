"""3000. Maximum Area of Longest Diagonal Rectangle"""

from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        diagonal_square_max = out = 0

        for length, width in dimensions:
            diagonal_square = length**2 + width**2

            if diagonal_square > diagonal_square_max:
                diagonal_square_max = diagonal_square
                out = length * width
            elif diagonal_square == diagonal_square_max:
                out = max(out, length * width)

        return out
