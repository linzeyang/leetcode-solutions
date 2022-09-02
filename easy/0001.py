"""
1. Two Sum
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range((length := len(nums)) - 1):
            b = target - nums[i]

            for j in range(i + 1, length):
                if nums[j] == b:
                    return [i, j]
