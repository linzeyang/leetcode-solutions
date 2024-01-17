"""198. House Robber"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums, default=0)

        dp: list[int] = [nums[0], nums[1], max(nums[0] + nums[2], nums[1])]

        for idx in range(3, len(nums)):
            dp.append(nums[idx] + max(dp[idx - 2], dp[idx - 3]))

        return max(dp)
