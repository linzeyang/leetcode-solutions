"""2016. Maximum Difference Between Increasing Elements"""

from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxx = 0

        for idx in range(len(nums) - 1):
            for jdx in range(idx + 1, len(nums)):
                if (diff := nums[jdx] - nums[idx]) > maxx:
                    maxx = diff

        if not maxx:
            return -1

        return maxx
