"""976. Largest Perimeter Triangle"""

from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)

        for idx in range(len(nums) - 2):
            if nums[idx] < nums[idx + 1] + nums[idx + 2]:
                return nums[idx] + nums[idx + 1] + nums[idx + 2]

        return 0
