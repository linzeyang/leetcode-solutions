"""807. Max Increase to Keep City Skyline"""

from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rows = [max(row) for row in grid]
        cols = [max(row[idx] for row in grid) for idx in range(len(grid[0]))]

        out = 0

        for idx, row in enumerate(grid):
            for jdx, block in enumerate(row):
                out += min(rows[idx], cols[jdx]) - block

        return out
