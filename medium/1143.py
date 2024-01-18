"""1143. Longest Common Subsequence"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp: list[list[int]] = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for idx in range(1, len(text1) + 1):
            for jdx in range(1, len(text2) + 1):
                if text1[idx - 1] == text2[jdx - 1]:
                    dp[idx][jdx] = dp[idx - 1][jdx - 1] + 1
                else:
                    dp[idx][jdx] = max(dp[idx][jdx - 1], dp[idx - 1][jdx])

        return dp[-1][-1]
