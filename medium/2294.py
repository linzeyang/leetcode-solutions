"""2294. Partition Array Such That Maximum Difference Is K"""

from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()

        out = 1
        pivot = nums[0]

        for idx in range(1, len(nums)):
            if nums[idx] - pivot > k:
                pivot = nums[idx]
                out += 1

        return out
