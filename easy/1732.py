"""1732. Find the Highest Altitude"""

from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = summ = 0

        for num in gain:
            summ += num
            if num > 0 and summ > highest:
                highest = summ

        return highest
