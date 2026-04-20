"""
2078. Two Furthest Houses With Different Colors

https://leetcode.com/problems/two-furthest-houses-with-different-colors/

Weekly Contest 268
"""

from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        first: int = colors[0]
        last: int = colors[-1]

        max_with_first: int = 0
        max_with_last: int = 0

        for idx, color in enumerate(reversed(colors)):
            if color != first:
                max_with_first = len(colors) - 1 - idx
                break

        for idx, color in enumerate(colors):
            if color != last:
                max_with_last = len(colors) - 1 - idx
                break

        return max(max_with_first, max_with_last)
