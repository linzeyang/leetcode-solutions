"""
628. Maximum Product of Three Numbers

https://leetcode.com/problems/maximum-product-of-three-numbers/
"""

from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]

        nums.sort()

        if nums[0] >= 0 or nums[-1] <= 0:
            return nums[-1] * nums[-2] * nums[-3]

        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
