"""3736. Minimum Moves to Equal Array Elements III"""

from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_num: int = max(nums)

        return sum(max_num - num for num in nums)
