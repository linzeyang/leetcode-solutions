"""1480. Running Sum of 1d Array"""

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        out: list[int] = [nums[0]]

        for idx in range(1, len(nums)):
            out.append(nums[idx] + out[-1])

        return out
