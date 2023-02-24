"""2367. Number of Arithmetic Triplets"""

from itertools import combinations
from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        out = 0

        for i, j, k in combinations(nums, 3):
            if i + diff == j == k - diff:
                out += 1

        return out
