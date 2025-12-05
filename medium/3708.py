"""3708. Longest Fibonacci Subarray"""

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        out: int = 2
        current: int = 2

        for idx in range(1, len(nums) - 1):
            if nums[idx - 1] + nums[idx] == nums[idx + 1]:
                current += 1
                out = max(out, current)
            else:
                current = 2

        return out
