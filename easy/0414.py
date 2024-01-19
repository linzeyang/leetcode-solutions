"""414. Third Maximum Number"""

from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        ss = sorted(set(nums))

        if len(ss) < 3:
            return ss[-1]

        return ss[-3]
