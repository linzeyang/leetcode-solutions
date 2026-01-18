"""3809. Best Reachable Tower"""

from typing import List


class Solution:
    """
    https://leetcode.com/problems/best-reachable-tower/
    Biweekly Contest 174
    """

    def bestTower(
        self, towers: List[List[int]], center: List[int], radius: int
    ) -> List[int]:
        maxq: int = -1
        maxxy: tuple = (float("inf"), float("inf"))

        for x, y, q in towers:
            if (abs(x - center[0]) + abs(y - center[1])) > radius:
                continue

            if q > maxq:
                maxq = q
                maxxy = (x, y)
            elif q == maxq:
                if (x, y) < maxxy:
                    maxxy = (x, y)

        if maxq == -1:
            return [-1, -1]

        return [maxxy[0], maxxy[1]]
