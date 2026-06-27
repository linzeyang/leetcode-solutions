"""
1189. Maximum Number of Balloons

https://leetcode.com/problems/maximum-number-of-balloons/

Weekly Contest 154
"""

from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter: Counter[str] = Counter(text)

        return min(
            counter["b"],
            counter["a"],
            counter["n"],
            counter["l"] // 2,
            counter["o"] // 2,
        )
