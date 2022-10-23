"""1979. Find Greatest Common Divisor of Array"""

from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        x, y = min(nums), max(nums)

        if y % x == 0:
            return x

        div = x // 2

        while div > 1:
            if x % div == 0 and y % div == 0:
                return div
            div -= 1

        return 1
