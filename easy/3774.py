"""3774. Absolute Difference Between Maximum and Minimum K Elements"""

from typing import List


class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        return abs(sum(nums[:k]) - sum(nums[-k:]))
