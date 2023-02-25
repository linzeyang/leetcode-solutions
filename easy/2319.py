"""2319. Check if Matrix Is X-Matrix"""

from typing import List


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        length = len(grid)

        for idx in range(length):
            for jdx, val in enumerate(grid[idx]):
                if jdx == idx or jdx == length - idx - 1:
                    if val == 0:
                        return False
                else:
                    if val != 0:
                        return False

        return True
