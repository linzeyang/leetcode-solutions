"""3622. Check Divisibility by Digit Sum and Product"""

from math import prod


class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits = [int(digit) for digit in list(str(n))]

        return n % (sum(digits) + prod(digits)) == 0
