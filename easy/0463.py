"""463. Island Perimeter"""

from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0

        for idx, row in enumerate(grid):
            for jdx, node in enumerate(row):
                if node:
                    perimeter += (
                        (jdx == 0 or grid[idx][jdx - 1] == 0)
                        + (jdx == len(row) - 1 or grid[idx][jdx + 1] == 0)
                        + (idx == 0 or grid[idx - 1][jdx] == 0)
                        + (idx == len(grid) - 1 or grid[idx + 1][jdx] == 0)
                    )

        return perimeter
