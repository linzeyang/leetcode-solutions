"""2023. Number of Pairs of Strings With Concatenation Equal to Target"""

from itertools import permutations
from typing import List


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        return sum(1 for x, y in permutations(nums, 2) if f"{x}{y}" == target)
