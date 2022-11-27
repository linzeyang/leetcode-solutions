"""2221. Find Triangular Sum of an Array"""

from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        while len(nums) > 1:
            new_array = []

            for i in range(len(nums) - 1):
                new_array.append((nums[i] + nums[i + 1]) % 10)

            nums = new_array

        return nums[0]
