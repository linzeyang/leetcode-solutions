"""1266. Minimum Time Visiting All Points"""

from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0

        out = 0

        for idx in range(1, len(points)):
            out += self._get_time(points[idx], points[idx - 1])

        return out

    def _get_time(self, point_a: list[int], point_b: list[int]) -> int:
        x_offset, y_offset = point_a[0] - point_b[0], point_a[1] - point_b[1]

        return max(abs(x_offset), abs(y_offset))
