"""75. Sort Colors"""

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]

        for num in nums:
            counts[num] += 1

        for idx in range(counts[0]):
            nums[idx] = 0

        for idx in range(counts[0], counts[0] + counts[1]):
            nums[idx] = 1

        for idx in range(counts[0] + counts[1], len(nums)):
            nums[idx] = 2
