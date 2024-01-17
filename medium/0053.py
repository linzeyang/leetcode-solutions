"""53. Maximum Subarray"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        out = current = nums[0]

        for idx in range(1, len(nums)):
            if current <= 0:
                current = nums[idx]
            else:
                current += nums[idx]

            if current > out:
                out = current

        return out
