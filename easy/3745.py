"""3745. Maximize Expression of Three Elements"""

from typing import List


class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        nums.sort()

        return nums[-1] + nums[-2] - nums[0]
