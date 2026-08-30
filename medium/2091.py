"""
2091. Removing Minimum and Maximum From Array

https://leetcode.com/problems/removing-minimum-and-maximum-from-array/

Weekly Contest 269
"""

from typing import List


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)

        min_idx: int = nums.index(min(nums))
        max_idx: int = nums.index(max(nums))

        low: int = min(min_idx, max_idx)
        high: int = max(min_idx, max_idx)

        return min(
            high + 1,
            len(nums) - low,
            len(nums) - high + low + 1,
        )
