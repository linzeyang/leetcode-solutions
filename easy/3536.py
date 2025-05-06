"""3536. Maximum Product of Two Digits"""


class Solution:
    def maxProduct(self, n: int) -> int:
        a, b = sorted(str(n))[-2:]

        return int(a) * int(b)
