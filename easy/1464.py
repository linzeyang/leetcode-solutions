"""1464. Maximum Product of Two Elements in an Array"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ll = sorted(nums)

        return (ll[-1] - 1) * (ll[-2] - 1)
