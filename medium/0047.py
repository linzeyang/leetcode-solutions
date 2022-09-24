"""
47. Permutations II
"""
from itertools import permutations
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Runtime: 66 ms, faster than 90.40% of Python3 online submissions for Permutations II.
        # Memory Usage: 14.3 MB, less than 50.00% of Python3 online submissions for Permutations II.
        ss = set()
        out = []

        for perm in permutations(nums, len(nums)):
            if perm not in ss:
                ss.add(perm)
                out.append(list(perm))

        return out
