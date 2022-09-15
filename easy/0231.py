"""
231. Power of Two
"""


# Using math.log2
class SolutionMath:
    def isPowerOfTwo(self, n: int) -> bool:
        # Runtime: 36 ms, faster than 89.63% of Python3 online submissions for Power of Two.
        # Memory Usage: 13.8 MB, less than 95.60% of Python3 online submissions for Power of Two.
        if n < 1:
            return False

        from math import log2

        return log2(n) % 1 == 0


# Using iteration
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Very slow:
        # Runtime: 67 ms, faster than 15.99% of Python3 online submissions for Power of Two.
        # Memory Usage: 13.8 MB, less than 95.60% of Python3 online submissions for Power of Two.
        if n < 1:
            return False

        while n > 1:
            if n % 2 == 1:
                return False
            n //= 2

        return True
