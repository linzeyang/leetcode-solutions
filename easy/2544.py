"""2544. Alternating Digit Sum"""


class Solution:
    def alternateDigitSum(self, n: int) -> int:
        sign = -1
        out = 0

        for char in str(n):
            out += -sign * int(char)
            sign *= -1

        return out
