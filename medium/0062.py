"""62. Unique Paths"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp: list[list[int]] = [[0] * n for _ in range(m)]

        for idx in range(n):
            dp[0][idx] = 1

        for jdx in range(m):
            dp[jdx][0] = 1

        for kdx in range(1, m):
            for ldx in range(1, n):
                dp[kdx][ldx] = dp[kdx - 1][ldx] + dp[kdx][ldx - 1]

        return dp[-1][-1]


class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1

        temp = list(range(1, n + 1))

        for _ in range(m - 2):
            for idx in range(1, n):
                temp[idx] += temp[idx - 1]

        return temp[-1]
