"""416. Partition Equal Subset Sum"""

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False

        summ = sum(nums)

        if summ & 1:
            return False

        target = summ // 2
        dp: list[list[bool]] = [[False] * (target + 1) for _ in range(len(nums))]

        if nums[0] <= target:
            dp[0][nums[0]] = True

        for idx in range(1, len(nums)):
            for jdx in range(1, target + 1):
                if dp[idx - 1][jdx] or nums[idx] == jdx:
                    dp[idx][jdx] = True
                elif nums[idx] > jdx:
                    dp[idx][jdx] = dp[idx - 1][jdx]
                else:
                    dp[idx][jdx] = dp[idx - 1][jdx - nums[idx]]

        return dp[len(nums) - 1][target]
