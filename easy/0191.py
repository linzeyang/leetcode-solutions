"""191. Number of 1 Bits"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        out = 0

        while n:
            n, mod = divmod(n, 2)
            if mod:
                out += 1

        return out
