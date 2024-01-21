"""64. Minimum Path Sum"""

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp: list[list[int]] = [[0] * len(grid[0]) for _ in range(len(grid))]

        dp[0][0] = grid[0][0]

        for idx in range(1, len(grid[0])):
            dp[0][idx] = grid[0][idx] + dp[0][idx - 1]

        for idx in range(1, len(grid)):
            for jdx in range(len(grid[0])):
                if jdx > 0:
                    prev = min(dp[idx - 1][jdx], dp[idx][jdx - 1])
                else:
                    prev = dp[idx - 1][jdx]

                dp[idx][jdx] = grid[idx][jdx] + prev

        return dp[-1][-1]
