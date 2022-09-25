"""80. Remove Duplicates from Sorted Array II"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # very slow:
        # Runtime: 124 ms, faster than 17.10% of Python3 online submissions for Remove Duplicates from Sorted Array II.
        # Memory Usage: 13.8 MB, less than 74.16% of Python3 online submissions for Remove Duplicates from Sorted Array II.
        if len(nums) < 3:
            return len(nums)

        base = nums[0]
        i = 1

        while i < len(nums):
            try:
                num = nums[i]
            except IndexError:
                break

            if i >= 2 and num == base and num == nums[i - 2]:
                nums.pop(i)
            else:
                base = num
                i += 1

        return len(nums)
