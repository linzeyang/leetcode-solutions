"""1800. Maximum Ascending Subarray Sum"""

from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        out = nums[0]
        summ = nums[0]

        for idx in range(1, len(nums)):
            if nums[idx] > nums[idx - 1]:
                summ += nums[idx]
            else:
                if summ > out:
                    out = summ
                summ = nums[idx]

        if summ > out:
            out = summ

        return out
