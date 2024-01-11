"""283. Move Zeroes"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        target_idx = 0

        for idx in range(len(nums)):
            if nums[idx]:
                if idx != target_idx:
                    nums[idx], nums[target_idx] = nums[target_idx], nums[idx]
                target_idx += 1
