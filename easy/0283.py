"""283. Move Zeroes"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        fast = slow = 0

        while fast < len(nums):
            if nums[fast] == 0:
                fast += 1
            else:
                if fast != slow:
                    nums[fast], nums[slow] = nums[slow], nums[fast]
                fast += 1
                slow += 1
