"""1317. Convert Integer to the Sum of Two No-Zero Integers"""

from typing import List


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        half = n // 2
        other = n - half

        while "0" in str(half) or "0" in str(other):
            half -= 1
            other += 1

        return [half, other]
