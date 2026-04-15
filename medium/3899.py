"""
3899. Angles of a Triangle

https://leetcode.com/problems/angles-of-a-triangle/

Weekly Contest 497
"""

from math import acos, degrees


class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        sides.sort()

        if sides[0] + sides[1] <= sides[2]:
            return []

        a, b, c = sides

        angles: list[float] = [
            round(degrees(acos((b**2 + c**2 - a**2) / (2 * b * c))), 5),
            round(degrees(acos((a**2 + c**2 - b**2) / (2 * a * c))), 5),
            round(degrees(acos((a**2 + b**2 - c**2) / (2 * a * b))), 5),
        ]

        return sorted(angles)
