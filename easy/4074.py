"""
4074. Maximum Product Pair With Target Sum

https://leetcode.com/problems/maximum-product-pair-with-target-sum/

Biweekly Contest 193
"""


class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        out: list[int] = [-1, -1]

        max_prod: int = -10_001

        register: dict[int, int] = {}

        for idx, num in enumerate(nums):
            if num * 2 == target:
                continue

            if (diff := target - num) not in register:
                register[num] = idx
            elif num * diff > max_prod:
                max_prod = num * diff

                if num > diff:
                    out = [idx, register[diff]]
                else:
                    out = [register[diff], idx]

        return out
