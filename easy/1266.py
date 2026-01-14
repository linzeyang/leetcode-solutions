"""1266. Minimum Time Visiting All Points"""

from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        out: int = 0

        for idx in range(1, len(points)):
            out += max(
                abs(points[idx][0] - points[idx - 1][0]),
                abs(points[idx][1] - points[idx - 1][1]),
            )

        return out
