"""
3993. Maximum Value of an Alternating Sequence

https://leetcode.com/problems/maximum-value-of-an-alternating-sequence/

Biweekly Contest 187
"""


class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        if n == 1:
            return s

        if n & 1:
            return s + m * (n // 2) - (n - 3) // 2

        return s + m * (n // 2) - (n - 2) // 2
