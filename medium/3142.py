"""3142. Check if Grid Satisfies Conditions"""

from typing import List


class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        row_0 = grid[0]

        for idx in range(len(row_0) - 1):
            if row_0[idx] == row_0[idx + 1]:
                return False

        for jdx in range(1, len(grid)):
            if grid[jdx] != row_0:
                return False

        return True
