"""2639. Find the Width of Columns of a Grid"""

from typing import List


class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        out = [0] * len(grid[0])

        for lis in grid:
            for col, num in enumerate(lis):
                out[col] = max(out[col], self._length(num))

        return out

    @staticmethod
    def _length(num: int) -> int:
        if num == 0:
            return 1

        out = num < 0
        num = abs(num)

        while num > 0:
            out += 1
            num //= 10

        return out
