"""693. Binary Number with Alternating Bits"""


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n == 1:
            return True

        if n % 2 == 0:
            n >>= 1

            if n % 2 == 0:
                return False

        while n > 0:
            n -= 1

            if n % 4 == 0:
                n >>= 2
            else:
                return False

        return True
