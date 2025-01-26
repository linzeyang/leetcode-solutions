"""2218. Maximum Value of K Coins From Piles"""

from typing import List


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)

        # 预先计算每个堆的前缀和
        prefix_sums = []

        for pile in piles:
            prefix = [0]

            for coin in pile:
                prefix.append(prefix[-1] + coin)

            prefix_sums.append(prefix)

        # 初始化 DP 表
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        # 填充 DP 表
        for i in range(1, n + 1):
            for j in range(k + 1):
                dp[i][j] = dp[i - 1][j]  # 不取当前堆的硬币

                # 尝试从当前堆取 t 个硬币
                max_t = min(len(piles[i - 1]), j)

                for t in range(1, max_t + 1):
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - t] + prefix_sums[i - 1][t])

        return dp[n][k]
