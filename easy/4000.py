"""
4000. Largest Integer With Given Digit Sum

https://leetcode.com/problems/largest-integer-with-given-digit-sum/

Weekly Contest 512
"""


class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s > n * 9:
            return -1

        out: int = 0

        for _ in range(n):
            out *= 10
            digit: int = min(s, 9)
            out += digit
            s -= digit

        return out
