"""840. Magic Squares In Grid"""

from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        width: int = len(grid[0])
        height: int = len(grid)

        if width < 3 or height < 3:
            return 0

        count: int = 0

        for idx in range(1, height - 1):
            for jdx in range(1, width - 1):
                if grid[idx][jdx] != 5:
                    continue

                # all 9 numbers should be distinct
                num_set: set[int] = {
                    grid[idx - 1][jdx - 1],
                    grid[idx - 1][jdx],
                    grid[idx - 1][jdx + 1],
                    grid[idx][jdx - 1],
                    grid[idx][jdx],
                    grid[idx][jdx + 1],
                    grid[idx + 1][jdx - 1],
                    grid[idx + 1][jdx],
                    grid[idx + 1][jdx + 1],
                }
                if num_set != set(range(1, 10)):
                    continue

                if grid[idx - 1][jdx - 1] + grid[idx + 1][jdx + 1] != 10:
                    continue
                if grid[idx - 1][jdx + 1] + grid[idx + 1][jdx - 1] != 10:
                    continue
                if grid[idx - 1][jdx] + grid[idx + 1][jdx] != 10:
                    continue
                if grid[idx][jdx - 1] + grid[idx][jdx + 1] != 10:
                    continue

                if (
                    grid[idx - 1][jdx - 1] + grid[idx - 1][jdx] + grid[idx - 1][jdx + 1]
                    != 15
                ):
                    continue
                if (
                    grid[idx + 1][jdx - 1] + grid[idx + 1][jdx] + grid[idx + 1][jdx + 1]
                    != 15
                ):
                    continue
                if (
                    grid[idx - 1][jdx - 1] + grid[idx][jdx - 1] + grid[idx + 1][jdx - 1]
                    != 15
                ):
                    continue
                if (
                    grid[idx - 1][jdx + 1] + grid[idx][jdx + 1] + grid[idx + 1][jdx + 1]
                    != 15
                ):
                    continue

                count += 1

        return count
