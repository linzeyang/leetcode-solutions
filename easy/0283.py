"""
283. Move Zeroes
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Slow:
        # Runtime: 378 ms, faster than 28.34% of Python3 online submissions for Move Zeroes.
        # Memory Usage: 15.6 MB, less than 64.75% of Python3 online submissions for Move Zeroes.
        zeroes_found = 0
        idx = 0

        while idx < len(nums) - zeroes_found:
            if nums[idx] != 0:
                idx += 1
                continue

            nums.pop(idx)
            nums.append(0)
            zeroes_found += 1
