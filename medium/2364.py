"""2364. Count Number of Bad Pairs"""

from math import comb
from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        mapping: dict[int, list[int]] = {}

        for idx, num in enumerate(nums):
            if (diff := num - idx) not in mapping:
                mapping[diff] = [idx]
            else:
                mapping[diff].append(idx)

        good = 0

        for lis in mapping.values():
            good += comb(len(lis), 2)

        return comb(len(nums), 2) - good
