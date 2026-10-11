"""
2778. Sum of Squares of Special Elements

https://leetcode.com/problems/sum-of-squares-of-special-elements/

Weekly Contest 354
"""

from typing import List


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        length: int = len(nums)

        return sum(num**2 for idx, num in enumerate(nums, start=1) if length % idx == 0)
