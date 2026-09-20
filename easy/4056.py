"""
4056. Number of Intersecting Interval Pairs I

https://leetcode.com/problems/number-of-intersecting-interval-pairs-i/

Weekly Contest 520
"""

from bisect import bisect


class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()

        out: int = 0

        for idx, interval in enumerate(intervals):
            jdx: int = bisect(intervals, [interval[1] + 1, 0])

            out += jdx - idx - 1

        return out
