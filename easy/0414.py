"""
414. Third Maximum Number
"""
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Slow:
        # Runtime: 110 ms, faster than 22.66% of Python3 online submissions for Third Maximum Number.
        # Memory Usage: 15.5 MB, less than 22.15% of Python3 online submissions for Third Maximum Number.
        ss = sorted(set(nums))

        if len(ss) < 3:
            return ss[-1]

        return ss[-3]
