"""2373. Largest Local Values in a Matrix"""

from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        out: list[list[int]] = [[] for _ in range(len(grid) - 2)]

        for idx in range(1, len(grid) - 1):
            for jdx in range(1, len(grid) - 1):
                out[idx - 1].append(
                    max(
                        grid[idx - 1][jdx - 1],
                        grid[idx - 1][jdx],
                        grid[idx - 1][jdx + 1],
                        grid[idx][jdx - 1],
                        grid[idx][jdx],
                        grid[idx][jdx + 1],
                        grid[idx + 1][jdx - 1],
                        grid[idx + 1][jdx],
                        grid[idx + 1][jdx + 1],
                    )
                )

        return out
