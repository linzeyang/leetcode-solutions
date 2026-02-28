"""1680. Concatenation of Consecutive Binary Numbers"""


class Solution:
    """
    https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/
    Weekly Contest 218
    """

    def concatenatedBinary(self, n: int) -> int:
        MOD: int = 10**9 + 7
        out: int = 0
        length: int = 0

        for i in range(1, n + 1):
            if (i & (i - 1)) == 0:
                length += 1

            out = ((out << length) | i) % MOD

        return out
