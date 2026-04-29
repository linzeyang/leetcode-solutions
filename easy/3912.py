"""
3912. Valid Elements in an Array

https://leetcode.com/problems/valid-elements-in-an-array/

Weekly Contest 499
"""


class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        left_maxs: list[int] = [0]
        right_maxs: list[int] = [0]

        for idx in range(len(nums) - 1):
            left_maxs.append(max(nums[idx], left_maxs[-1]))

        for idx in range(len(nums) - 1):
            right_maxs.append(max(nums[-idx - 1], right_maxs[-1]))

        out: list[int] = []

        for idx, num in enumerate(nums):
            if num > left_maxs[idx] or num > right_maxs[-idx - 1]:
                out.append(num)

        return out
