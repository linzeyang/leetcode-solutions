"""231. Power of Two"""


# Using math.log2
class SolutionMath:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False

        from math import log2

        return log2(n) % 1 == 0


# Using iteration
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False

        while n > 1:
            if n & 1 == 1:
                return False
            n >>= 1

        return True


class Solution3:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        return bin(n).count("1") == 1
