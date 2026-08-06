"""
3345. Smallest Divisible Digit Product I

https://leetcode.com/problems/smallest-divisible-digit-product-i/

Biweekly Contest 143
"""

from math import prod


class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        if t == 1:
            return n

        while (self._get_prod(num=n) % t) != 0:
            n += 1

        return n

    @staticmethod
    def _get_prod(num: int) -> int:
        return prod(int(digit) for digit in str(num))
