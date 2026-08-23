"""
3622. Check Divisibility by Digit Sum and Product

https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/

Weekly Contest 459
"""

from math import prod


class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits: list[int] = [int(digit) for digit in list(str(n))]

        return n % (sum(digits) + prod(digits)) == 0
