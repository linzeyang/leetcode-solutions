"""1913. Maximum Product Difference Between Two Pairs"""

from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        ss = sorted(nums)

        return ss[-1] * ss[-2] - ss[0] * ss[1]
