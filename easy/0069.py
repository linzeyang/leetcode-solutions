"""
69. Sqrt(x)
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        # Very slow:
        # Runtime: 5064 ms, faster than 5.54% of Python3 online submissions for Sqrt(x).
        # Memory Usage: 13.8 MB, less than 56.60% of Python3 online submissions for Sqrt(x).

        if x in {0, 1}:
            return x

        num = x // 2

        while (numsqr := num**2) >= x:
            if numsqr == x:
                return num
            num //= 2

        i = 2 * num + 1

        while i > 0:
            i -= 1

            if i**2 <= x:
                return i
