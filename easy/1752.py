"""1752. Check if Array Is Sorted and Rotated"""

from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        length = len(nums)

        if length == 1:
            return True

        for idx in range(1, length):
            if nums[idx] < nums[idx - 1]:
                break
        else:
            return True

        for jdx in range(idx + 1, length):
            if nums[jdx] < nums[jdx - 1]:
                return False

        return nums[-1] <= nums[0]
