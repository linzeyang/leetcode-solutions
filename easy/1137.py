"""1137. N-th Tribonacci Number"""


class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0

        if n in {1, 2}:
            return 1

        a, b, c = 0, 1, 1

        for _ in range(n - 2):
            out = a + b + c
            a, b, c = b, c, out

        return out
