"""190. Reverse Bits"""


class Solution:
    def reverseBits(self, n: int) -> int:
        out = 0

        for _ in range(32):
            if n > 0:
                n, mod = divmod(n, 2)
                out = (out << 1) + mod
            else:
                out <<= 1

        return out
