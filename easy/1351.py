"""1351. Count Negative Numbers in a Sorted Matrix"""

from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        out = 0

        rows = len(grid)
        columns = len(grid[0])

        ro = 0

        for i in range(-1, -columns - 1, -1):
            for j in range(ro, rows):
                if grid[j][i] < 0:
                    out += rows - j
                    ro = j
                    break

                ro = j

        return out
