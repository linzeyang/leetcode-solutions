"""2348. Number of Zero-Filled Subarrays"""

from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        zero = out = 0

        for num in nums:
            if num == 0:
                zero += 1
            elif zero:
                out += self._count(zero)
                zero = 0

        if num == 0:
            out += self._count(zero)

        return out

    def _count(self, n: int) -> int:
        return (n + 1) * n // 2
