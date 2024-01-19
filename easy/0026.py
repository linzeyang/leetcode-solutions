"""26. Remove Duplicates from Sorted Array"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if (length := len(nums)) in {0, 1}:
            return length

        base = nums[0]

        index = 1

        while len(nums) >= index + 1:
            if nums[index] == base:
                nums.pop(index)
            else:
                base = nums[index]
                index += 1

        return len(nums)
