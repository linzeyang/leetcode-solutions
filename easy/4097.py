"""
4097. Minimum Value of Merged Integers

https://leetcode.com/problems/minimum-value-of-merged-integers/

Weekly Contest 526
"""


class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        out: int = -1

        for idx in range(0, len(nums), 2):
            merged: int = int(str(nums[idx]) + str(nums[idx + 1]))

            if out == -1:
                out = merged
            else:
                out = min(out, merged)

        return out
