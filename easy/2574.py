"""
2574. Left and Right Sum Differences

https://leetcode.com/problems/left-and-right-sum-differences/

Weekly Contest 334
"""

from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum: int = 0
        right_sum: int = sum(nums)

        out: list[int] = []

        for val in nums:
            right_sum -= val
            out.append(abs(left_sum - right_sum))
            left_sum += val

        return out
