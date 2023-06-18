"""2740. Find the Value of the Partition"""

from typing import List


class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums = sorted(nums)
        out = nums[1] - nums[0]

        for idx in range(2, len(nums)):
            if (diff := nums[idx] - nums[idx - 1]) < out:
                out = diff

        return out
