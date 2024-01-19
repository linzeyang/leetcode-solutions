"""931. Minimum Falling Path Sum"""

from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp: list[list[int]] = [[0] * len(matrix) for _ in range(len(matrix))]

        for idx in range(len(matrix)):
            dp[0][idx] = matrix[0][idx]

        for idx in range(1, len(matrix)):
            for jdx in range(len(matrix)):
                if 0 < jdx < len(matrix) - 1:
                    prev = min(dp[idx - 1][jdx - 1 : jdx + 2])
                elif jdx == 0:
                    prev = min(dp[idx - 1][jdx : jdx + 2])
                else:
                    prev = min(dp[idx - 1][jdx - 1 : jdx + 1])

                dp[idx][jdx] = prev + matrix[idx][jdx]

        return min(dp[-1])
