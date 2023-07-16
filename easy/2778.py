"""2778. Sum of Squares of Special Elements"""

from typing import List


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        length = len(nums)

        return sum(num**2 for idx, num in enumerate(nums) if length % (idx + 1) == 0)
