""""""

from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        num_of_islands = 0

        for idx, row in enumerate(grid):
            for jdx, node in enumerate(row):
                if node == 0 and self._flood(grid, idx, jdx):
                    num_of_islands += 1

        return num_of_islands

    def _flood(self, grid: list[list[int]], idx: int, jdx: int) -> bool:
        grid[idx][jdx] = 1

        if idx >= 1 and grid[idx - 1][jdx] == 0:
            res1 = self._flood(grid, idx - 1, jdx)
        else:
            res1 = True
        if idx < len(grid) - 1 and grid[idx + 1][jdx] == 0:
            res2 = self._flood(grid, idx + 1, jdx)
        else:
            res2 = True
        if jdx >= 1 and grid[idx][jdx - 1] == 0:
            res3 = self._flood(grid, idx, jdx - 1)
        else:
            res3 = True
        if jdx < len(grid[0]) - 1 and grid[idx][jdx + 1] == 0:
            res4 = self._flood(grid, idx, jdx + 1)
        else:
            res4 = True

        res = not (idx in (0, len(grid) - 1) or jdx in (0, len(grid[0]) - 1))

        return res and res1 and res2 and res3 and res4
