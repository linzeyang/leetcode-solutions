"""
1288. Remove Covered Intervals

https://leetcode.com/problems/remove-covered-intervals/

Biweekly Contest 15
"""

from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: (interval[0], -interval[1]))

        out: int = 0
        max_end: int = 0

        for _, end in intervals:
            if end > max_end:
                out += 1
                max_end = end

        return out
