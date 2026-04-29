"""
3914. Minimum Operations to Make Array Non Decreasing

https://leetcode.com/problems/minimum-operations-to-make-array-non-decreasing/

Weekly Contest 499
"""


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        out: int = 0

        for idx in range(len(nums) - 1):
            if nums[idx] > nums[idx + 1]:
                out += nums[idx] - nums[idx + 1]

        return out
