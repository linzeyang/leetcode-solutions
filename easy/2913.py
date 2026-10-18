"""
2913. Subarrays Distinct Element Sum of Squares I

https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/

Biweekly Contest 116
"""

from typing import List


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        count: int = 0

        for idx, num in enumerate(nums):
            sett: set[int] = {num}
            count += 1

            for jdx in range(idx + 1, len(nums)):
                sett.add(nums[jdx])
                count += len(sett) ** 2

        return count
