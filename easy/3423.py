"""3423. Maximum Difference Between Adjacent Elements in a Circular Array"""

from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        out = -1

        if len(nums) == 2:
            return abs(nums[0] - nums[1])

        for idx, num in enumerate(nums):
            if idx == len(nums) - 1:
                diff = abs(num - nums[0])
            else:
                diff = abs(num - nums[idx + 1])

            out = max(out, diff)

        return out
