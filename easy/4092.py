"""
4092. Binary Digit Score

https://leetcode.com/problems/binary-digit-score/

Weekly Contest 525
"""


class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        s1: int = bin(a).count("1")
        s2: int = bin(b).count("1")

        if s1 >= s2:
            return s1 * s2

        return s2 // s1
