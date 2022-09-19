"""
342. Power of Four
"""


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Runtime: 50 ms, faster than 53.38% of Python3 online submissions for Power of Four.
        # Memory Usage: 13.8 MB, less than 94.93% of Python3 online submissions for Power of Four.
        if n <= 0:
            return False

        if n == 1:
            return True

        if n % 4 != 0:
            return False

        return self.isPowerOfFour(n // 4)
