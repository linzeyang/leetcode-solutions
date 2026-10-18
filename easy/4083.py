"""
4083. Minimum Deletions to Make Array Sharp

https://leetcode.com/problems/minimum-deletions-to-make-array-sharp/

Weekly Contest 524
"""


class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        out: int = 0
        local: int = 1

        for idx in range(1, len(nums)):
            if nums[idx] == nums[idx - 1]:
                local += 1
            else:
                out += local - 1
                local = 1

        out += local - 1

        return out
