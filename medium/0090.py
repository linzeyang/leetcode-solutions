"""90. Subsets II"""

from itertools import combinations
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Slow:
        # Runtime: 77 ms, faster than 24.35% of Python3 online submissions for Subsets II.
        # Memory Usage: 14 MB, less than 93.89% of Python3 online submissions for Subsets II.
        out = []
        nums.sort()

        for i in range(len(nums) + 1):
            ss = set()
            for comb in combinations(nums, i):
                if comb not in ss:
                    ss.add(comb)
                    out.append(list(comb))

        return out
