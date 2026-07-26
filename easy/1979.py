"""
1979. Find Greatest Common Divisor of Array

https://leetcode.com/problems/find-greatest-common-divisor-of-array/

Weekly Contest 255
"""

import math
from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        x: int = min(nums)
        y: int = max(nums)

        if y % x == 0:
            return x

        div: int = x // 2

        while div > 1:
            if x % div == 0 and y % div == 0:
                return div
            div -= 1

        return 1


class Solution2:
    def findGCD(self, nums: List[int]) -> int:
        return math.gcd(min(nums), max(nums))
