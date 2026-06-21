"""
1344. Angle Between Hands of a Clock

https://leetcode.com/problems/angle-between-hands-of-a-clock/

Biweekly Contest 19
"""


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        min_degree: float = minutes * 6.0
        hour_degree: float = (hour % 12) * 30 + minutes / 2

        degree: float = abs(min_degree - hour_degree)

        if degree > 180:
            degree = 360 - degree

        return degree
