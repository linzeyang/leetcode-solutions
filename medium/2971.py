"""2971. Find Polygon With the Largest Perimeter"""

from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        summ = sum(nums)
        nums.sort(reverse=True)

        for idx in range(len(nums) - 2):
            if nums[idx] < summ / 2:
                return summ

            summ -= nums[idx]

        return -1
