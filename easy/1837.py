"""1837. Sum of Digits in Base K"""


class Solution:
    def sumBase(self, n: int, k: int) -> int:
        out = 0

        while n > 0:
            quo, rem = divmod(n, k)
            out += rem
            n = quo

        return out
