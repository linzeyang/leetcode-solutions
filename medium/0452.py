"""452. Minimum Number of Arrows to Burst Balloons"""

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1

        points.sort(key=lambda point: point[1])
        out = 1
        ending = points[0][1]

        for idx in range(1, len(points)):
            if points[idx][0] <= ending:
                continue

            ending = points[idx][1]
            out += 1

        return out
