"""908. Smallest Range I"""

from typing import List


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0

        min_num = min(nums)
        max_num = max(nums)

        if max_num - min_num <= 2 * k:
            return 0

        return max_num - min_num - 2 * k
