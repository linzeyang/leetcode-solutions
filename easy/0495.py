"""495. Teemo Attacking"""

from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        out = 0
        end = -1

        for time in timeSeries:
            if time > end:
                out += duration
            else:
                out += time + duration - 1 - end

            end = time + duration - 1

        return out
