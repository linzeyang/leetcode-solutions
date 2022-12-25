"""628. Maximum Product of Three Numbers"""

from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return nums[0] * nums[1] * nums[2]

        ll = sorted(nums)

        if ll[0] >= 0 or ll[-1] <= 0:
            return ll[-1] * ll[-2] * ll[-3]

        return max(ll[-1] * ll[-2] * ll[-3], ll[0] * ll[1] * ll[-1])
