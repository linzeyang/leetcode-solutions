"""
217. Contains Duplicate
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Runtime: 1053 ms, faster than 9.86% of Python3 online submissions for Contains Duplicate.
        # Memory Usage: 26 MB, less than 28.10% of Python3 online submissions for Contains Duplicate.
        return len(set(nums)) < len(nums)
