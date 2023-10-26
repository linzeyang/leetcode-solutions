"""1020. Number of Enclaves"""

from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        num_of_enclaves = 0

        for idx, row in enumerate(grid):
            for jdx, node in enumerate(row):
                if node:
                    num, is_enclave = self._flood(grid, idx, jdx)
                    num_of_enclaves += is_enclave * num

        return num_of_enclaves

    def _flood(self, grid: list[list[int]], idx: int, jdx: int) -> tuple[int, bool]:
        grid[idx][jdx] = 0
        num = 1

        if idx in (0, len(grid) - 1) or jdx in (0, len(grid[0]) - 1):
            res = False
        else:
            res = True

        if idx >= 1 and grid[idx - 1][jdx]:
            num1, res1 = self._flood(grid, idx - 1, jdx)
            num += res1 * num1
            res = res and res1
        if idx < len(grid) - 1 and grid[idx + 1][jdx]:
            num2, res2 = self._flood(grid, idx + 1, jdx)
            num += res2 * num2
            res = res and res2
        if jdx >= 1 and grid[idx][jdx - 1]:
            num3, res3 = self._flood(grid, idx, jdx - 1)
            num += res3 * num3
            res = res and res3
        if jdx < len(grid[0]) - 1 and grid[idx][jdx + 1]:
            num4, res4 = self._flood(grid, idx, jdx + 1)
            num += res4 * num4
            res = res and res4

        return num, res
