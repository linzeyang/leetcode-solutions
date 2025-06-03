"""883. Projection Area of 3D Shapes"""

from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        num_xy = 0
        zx_proj: list[int] = [0] * len(grid)
        zy_proj: list[int] = [0] * len(grid[0])

        for idx, row in enumerate(grid):
            zx_proj[idx] = max(row)

            for jdx, height in enumerate(row):
                if not height:
                    continue

                num_xy += 1
                zy_proj[jdx] = max(zy_proj[jdx], height)

        return sum(zx_proj) + sum(zy_proj) + num_xy
