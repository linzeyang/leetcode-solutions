"""2154. Keep Multiplying Found Values by Two"""

from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums_set: set[int] = set(nums)

        while original in nums_set:
            original *= 2

        return original
