"""
4044. Count Good Cyclic Rotations

https://leetcode.com/problems/count-good-cyclic-rotations/

Weekly Contest 518
"""


class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        length: int = len(nums)

        diff: int = sum(nums[: length // 2]) - sum(nums[length // 2 :])

        out: int = int(diff > 0)

        for idx in range(length - 1):
            a: int = nums[idx]
            b: int = nums[(idx + length // 2) % length]

            diff -= (a - b) * 2

            if diff > 0:
                out += 1

        return out
