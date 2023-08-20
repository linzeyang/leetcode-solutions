"""2824. Count Pairs Whose Sum is Less than Target"""

from itertools import combinations
from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        return sum(1 for i, j in combinations(nums, 2) if i + j < target)
