"""300. Longest Increasing Subsequence"""

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp: list[int] = [1]

        for idx in range(1, len(nums)):
            count = 1

            for jdx in range(idx - 1, -1, -1):
                if nums[idx] > nums[jdx] and dp[jdx] + 1 > count:
                    count = dp[jdx] + 1

            dp.append(count)

        return max(dp)
