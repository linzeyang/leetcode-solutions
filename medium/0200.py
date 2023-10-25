"""200. Number of Islands"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_of_islands = 0

        for idx, row in enumerate(grid):
            for jdx, node in enumerate(row):
                if node == "1":
                    num_of_islands += 1
                    self._flood(grid, idx, jdx)

        return num_of_islands

    def _flood(self, grid: list[list[str]], idx: int, jdx: int) -> None:
        grid[idx][jdx] = "0"

        if idx >= 1 and grid[idx - 1][jdx] == "1":
            self._flood(grid, idx - 1, jdx)
        if idx < len(grid) - 1 and grid[idx + 1][jdx] == "1":
            self._flood(grid, idx + 1, jdx)
        if jdx >= 1 and grid[idx][jdx - 1] == "1":
            self._flood(grid, idx, jdx - 1)
        if jdx < len(grid[0]) - 1 and grid[idx][jdx + 1] == "1":
            self._flood(grid, idx, jdx + 1)
