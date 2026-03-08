"""190. Reverse Bits"""


class Solution:
    """
    https://leetcode.com/problems/reverse-bits/
    """

    def reverseBits(self, n: int) -> int:
        out: int = 0

        for _ in range(32):
            if n > 0:
                n, mod = divmod(n, 2)
                out = (out << 1) + mod
            else:
                out <<= 1

        return out


class Solution2:
    def reverseBits(self, n: int) -> int:
        return int(f"{n:0>32b}"[::-1], base=2)
