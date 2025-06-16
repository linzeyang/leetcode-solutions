"""2016. Maximum Difference Between Increasing Elements"""

from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        out = -1
        current_min = 1_000_000_000 + 1

        for idx in range(len(nums) - 1):
            current_min = min(current_min, nums[idx])

            if nums[idx + 1] > current_min:
                out = max(out, nums[idx + 1] - current_min)

        return out
