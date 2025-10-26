"""3718. Smallest Missing Multiple of K"""

from typing import List


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums_set: set[int] = set(nums)

        for fac in range(1, 102):
            if k * fac not in nums_set:
                return k * fac

        return -1
