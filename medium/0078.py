"""
78. Subsets
"""

from itertools import combinations
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Very slow:
        # Runtime: 79 ms, faster than 6.40% of Python3 online submissions for Subsets.
        # Memory Usage: 14 MB, less than 82.64% of Python3 online submissions for Subsets.
        out = [[]]

        for i in range(1, len(nums) + 1):
            out.extend([list(combo) for combo in combinations(nums, i)])

        return out
