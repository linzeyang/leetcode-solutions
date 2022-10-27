"""2154. Keep Multiplying Found Values by Two"""

from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while original in nums:
            original *= 2

        return original
