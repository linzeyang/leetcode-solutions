"""1995. Count Special Quadruplets"""

from itertools import combinations
from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        out = 0

        for a, b, c, d in combinations(nums, 4):
            if a + b + c == d:
                out += 1

        return out
