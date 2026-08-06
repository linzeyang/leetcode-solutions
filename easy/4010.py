"""
4010. Maximize Pair Strength Using GCD

https://leetcode.com/problems/maximize-pair-strength-using-gcd/

Weekly Contest 513
"""

from math import gcd


class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        out: int = 0

        for idx in range(len(nums) - 1):
            for jdx in range(idx + 1, len(nums)):
                strength: int = (nums[idx] * nums[jdx]) // gcd(
                    nums[idx], nums[jdx]
                ) ** 2

                out = max(out, strength)

        return out
