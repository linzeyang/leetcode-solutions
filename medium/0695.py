"""695. Max Area of Island"""

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxx = 0

        for idx, row in enumerate(grid):
            for jdx, node in enumerate(row):
                if node and (flooded := self._flood(grid, idx, jdx)) > maxx:
                    maxx = flooded

        return maxx

    def _flood(self, grid: list[list[int]], idx: int, jdx: int) -> int:
        grid[idx][jdx] = 0
        flooded = 1

        if idx >= 1 and grid[idx - 1][jdx]:
            flooded += self._flood(grid, idx - 1, jdx)
        if idx < len(grid) - 1 and grid[idx + 1][jdx]:
            flooded += self._flood(grid, idx + 1, jdx)
        if jdx >= 1 and grid[idx][jdx - 1]:
            flooded += self._flood(grid, idx, jdx - 1)
        if jdx < len(grid[0]) - 1 and grid[idx][jdx + 1]:
            flooded += self._flood(grid, idx, jdx + 1)

        return flooded
