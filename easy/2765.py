"""2765. Longest Alternating Subarray"""

from typing import List


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        dp: list[int] = [0, 2 if nums[1] - nums[0] == 1 else 0]

        for idx in range(2, len(nums)):
            if nums[idx] - nums[idx - 1] == 1:
                if dp[idx - 1] > 0 and nums[idx - 2] - nums[idx - 1] == 1:
                    dp.append(dp[idx - 1] + 1)
                else:
                    dp.append(2)
            elif nums[idx] - nums[idx - 1] == nums[idx - 2] - nums[idx - 1] == -1:
                dp.append(dp[idx - 1] + 1)
            else:
                dp.append(0)

        return max(dp) or -1
