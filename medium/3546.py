"""3546. Equal Sum Grid Partition I"""

from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum(sum(row) for row in grid)

        if total & 1:
            return False

        # rows
        current = 0

        for row in grid:
            current += sum(row)

            if current == total // 2:
                return True
            if current > total // 2:
                break

        # columns
        current = 0

        for jdx in range(len(grid[0])):
            current += sum(row[jdx] for row in grid)

            if current == total // 2:
                return True
            if current > total // 2:
                return False

        return False
