"""3345. Smallest Divisible Digit Product I"""

from math import prod


class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        if t == 1:
            return n

        while n:
            if self._get_prod(n) % t != 0:
                n += 1
                continue

            break

        return n

    @staticmethod
    def _get_prod(num: int) -> int:
        return prod(int(digit) for digit in str(num))
