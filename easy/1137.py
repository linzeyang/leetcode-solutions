"""1137. N-th Tribonacci Number"""


class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n

        a, b, c = 0, 1, 1

        while n > 2:
            a, b, c = b, c, a + b + c
            n -= 1

        return c
