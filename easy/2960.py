"""2960. Count Tested Devices After Test Operations"""

from typing import List


class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        out = 0

        for per in batteryPercentages:
            if per > out:
                out += 1

        return out
