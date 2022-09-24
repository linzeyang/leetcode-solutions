"""
46. Permutations
"""
from itertools import permutations
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Very slow:
        # Runtime: 89 ms, faster than 11.71% of Python3 online submissions for Permutations.
        # Memory Usage: 14 MB, less than 58.57% of Python3 online submissions for Permutations.
        return [list(perm) for perm in permutations(nums, len(nums))]
