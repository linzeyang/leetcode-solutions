"""3678. Smallest Absent Positive Greater Than Average"""

from typing import List


class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        avg: int = int(sum(nums) / len(nums))
        target: int = max(avg + 1, 1)

        nums_set: set[int] = set(nums)

        while target in nums_set:
            target += 1

        return target
