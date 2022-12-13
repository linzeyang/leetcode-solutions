"""2500. Delete Greatest Value in Each Row"""

from typing import List


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        out = 0

        for row in grid:
            row.sort()

        for idx in range(len(grid[0])):
            out += max(r[idx] for r in grid)

        return out
