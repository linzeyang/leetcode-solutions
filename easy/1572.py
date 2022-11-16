"""1572. Matrix Diagonal Sum"""

from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        length = len(mat)

        if length == 1:
            return mat[0][0]

        out = 0

        for i in range(length):
            if i != length - i - 1:
                out += mat[i][i] + mat[i][-i - 1]
            else:
                out += mat[i][i]

        return out
