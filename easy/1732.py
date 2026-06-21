"""
1732. Find the Highest Altitude

https://leetcode.com/problems/find-the-highest-altitude/

Biweekly Contest 44
"""

from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_altitude: int = 0
        max_altitude: int = 0

        for alt in gain:
            current_altitude += alt
            max_altitude = max(max_altitude, current_altitude)

        return max_altitude
