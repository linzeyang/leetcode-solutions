"""1828. Queries on Number of Points Inside a Circle"""

from typing import List


class Solution:
    def countPoints(
        self, points: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        return [
            sum(
                1
                for coord_x, coord_y in points
                if (coord_x - cen_x) ** 2 + (coord_y - cen_y) ** 2 <= radius**2
            )
            for cen_x, cen_y, radius in queries
        ]
