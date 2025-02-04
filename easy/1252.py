"""1252. Cells with Odd Values in a Matrix"""

from typing import List


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows: list[int] = [0] * m
        cols: list[int] = [0] * n

        for row, col in indices:
            rows[row] ^= 1
            cols[col] ^= 1

        out = 0

        for idx in range(m):
            for jdx in range(n):
                if rows[idx] + cols[jdx] == 1:
                    out += 1

        return out
