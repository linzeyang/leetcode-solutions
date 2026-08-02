"""
3536. Maximum Product of Two Digits

https://leetcode.com/problems/maximum-product-of-two-digits/

Weekly Contest 448
"""


class Solution:
    def maxProduct(self, n: int) -> int:
        a, b = sorted(str(n))[-2:]

        return int(a) * int(b)
