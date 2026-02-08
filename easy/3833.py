"""3833. Count Dominant Indices"""

from typing import List


class Solution:
    """
    https://leetcode.com/problems/count-dominant-indices/
    Weekly Contest 488
    """

    def dominantIndices(self, nums: List[int]) -> int:
        length: int = len(nums)

        if length == 1:
            return 0

        out: int = 0
        current_sum: int = nums[-1]

        for idx in range(2, length + 1):
            if nums[-idx] * (idx - 1) > current_sum:
                out += 1

            current_sum += nums[-idx]

        return out
