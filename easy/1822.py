"""1822. Sign of the Product of an Array"""

from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign = 1

        for num in nums:
            if num > 0:
                sign *= 1
            elif num < 0:
                sign *= -1
            else:
                return 0

        return sign
