"""72. Edit Distance"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp: list[list[int]] = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for n in range(len(word2) + 1):
            dp[0][n] = n

        for n in range(len(word1) + 1):
            dp[n][0] = n

        for idx in range(1, len(word1) + 1):
            for jdx in range(1, len(word2) + 1):
                if word1[idx - 1] == word2[jdx - 1]:
                    dp[idx][jdx] = dp[idx - 1][jdx - 1]
                else:
                    dp[idx][jdx] = (
                        min(
                            dp[idx - 1][jdx - 1],
                            dp[idx - 1][jdx],
                            dp[idx][jdx - 1],
                        )
                        + 1
                    )

        return dp[-1][-1]
