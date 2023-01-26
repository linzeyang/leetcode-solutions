"""1037. Valid Boomerang"""

from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        p1, p2, p3 = points[0], points[1], points[2]

        if p1 == p2 or p2 == p3 or p1 == p3:
            return False

        if p1[0] == p2[0] == p3[0] or p1[1] == p2[1] == p3[1]:
            return False

        try:
            return (p1[0] - p2[0]) / (p1[1] - p2[1]) != (p1[0] - p3[0]) / (
                p1[1] - p3[1]
            )
        except ZeroDivisionError:
            return True
