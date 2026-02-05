"""3637. Trionic Array I"""

from typing import List


class Solution:
    """
    https://leetcode.com/problems/trionic-array-i/
    Weekly Contest 461
    """

    def isTrionic(self, nums: List[int]) -> bool:
        length: int = len(nums)

        if length < 4:
            return False

        if nums[1] <= nums[0]:
            return False

        # look for p
        for idx in range(2, length - 1):
            if nums[idx] < nums[idx - 1]:
                break
            if nums[idx] == nums[idx - 1]:
                return False
        else:
            return False

        # look for q
        for jdx in range(idx + 1, length):
            if nums[jdx] > nums[jdx - 1]:
                break
            if nums[jdx] == nums[jdx - 1]:
                return False
        else:
            return False

        for kdx in range(jdx + 1, length):
            if nums[kdx] <= nums[kdx - 1]:
                return False

        return True
