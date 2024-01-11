"""1822. Sign of the Product of an Array"""

from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign = 1

        for num in nums:
            if not num:
                return 0

            if num < 0:
                sign = -sign

        return sign
