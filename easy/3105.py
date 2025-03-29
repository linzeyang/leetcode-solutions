"""3105. Longest Strictly Increasing or Strictly Decreasing Subarray"""

from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_inc = current = 1

        for idx in range(1, len(nums)):
            if nums[idx] > nums[idx - 1]:
                current += 1
            else:
                max_inc = max(max_inc, current)
                current = 1

        max_inc = max(max_inc, current)

        max_dec = current = 1

        for idx in range(1, len(nums)):
            if nums[idx] < nums[idx - 1]:
                current += 1
            else:
                max_dec = max(max_dec, current)
                current = 1

        max_dec = max(max_dec, current)

        return max(max_inc, max_dec)
