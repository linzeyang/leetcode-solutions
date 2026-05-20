"""
2784. Check if Array is Good

https://leetcode.com/problems/check-if-array-is-good/description/

Biweekly Contest 109
"""

from typing import List


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        length: int = len(nums)

        if length == 1:
            return False

        nums.sort()

        for idx in range(length - 1):
            if nums[idx] != idx + 1:
                return False

        if nums[-1] != nums[-2]:
            return False

        return True
