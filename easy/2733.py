"""2733. Neither Minimum nor Maximum"""

from typing import List


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return -1

        min_max = (min(nums), max(nums))

        for num in nums:
            if num not in min_max:
                return num

        return -1
