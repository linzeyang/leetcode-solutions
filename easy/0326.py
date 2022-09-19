"""
326. Power of Three
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Runtime: 166 ms, faster than 24.51% of Python3 online submissions for Power of Three.
        # Memory Usage: 13.9 MB, less than 58.08% of Python3 online submissions for Power of Three.
        if n <= 0:
            return False

        if n == 1:
            return True

        if n % 3 != 0:
            return False

        return self.isPowerOfThree(n // 3)
