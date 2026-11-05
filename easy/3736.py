"""
3736. Minimum Moves to Equal Array Elements III

https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/

Biweekly Contest 169
"""

from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_num: int = max(nums)

        return sum(max_num - num for num in nums)
