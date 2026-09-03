"""
3718. Smallest Missing Multiple of K

https://leetcode.com/problems/smallest-missing-multiple-of-k/

Weekly Contest 472
"""

from typing import List


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums_set: set[int] = set(nums)

        for fac in range(1, len(nums) + 1):
            if k * fac not in nums_set:
                return k * fac

        return k * (len(nums) + 1)
