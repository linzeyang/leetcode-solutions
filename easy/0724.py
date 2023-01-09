"""
724. Find Pivot Index
This question is the same as 1991
"""

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        length = len(nums)

        if length == 1:
            return 0

        summ = sum(nums)

        if nums[0] == summ:
            return 0

        sub_total = nums[0]

        for i in range(1, length):
            if sub_total * 2 == summ - nums[i]:
                return i

            sub_total += nums[i]

        return -1
