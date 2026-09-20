"""
3498. Reverse Degree of a String

https://leetcode.com/problems/reverse-degree-of-a-string

Biweekly Contest 153
"""


class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum(
            (26 - ord(char) + ord("a")) * (idx + 1) for idx, char in enumerate(s)
        )
