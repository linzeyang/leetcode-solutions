"""3392. Count Subarrays of Length Three With a Condition"""

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        out = 0

        for idx in range(1, len(nums) - 1):
            if nums[idx] & 1 == 1:
                continue

            if (nums[idx - 1] + nums[idx + 1]) * 2 == nums[idx]:
                out += 1

        return out
