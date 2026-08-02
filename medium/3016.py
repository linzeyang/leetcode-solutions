"""
3016. Minimum Number of Pushes to Type Word II

https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

Weekly Contest 381
"""

from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        return sum(
            counts * (idx // 8 + 1)
            for idx, counts in enumerate(sorted(Counter(word).values(), reverse=True))
        )
