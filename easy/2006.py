"""2006. Count Number of Pairs With Absolute Difference K"""

from itertools import combinations
from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        return len([x for x, y in combinations(nums, 2) if abs(x - y) == k])
