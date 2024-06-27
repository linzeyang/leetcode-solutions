"""3184. Count Pairs That Form a Complete Day I"""

from typing import List


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        out = 0

        for idx in range(len(hours) - 1):
            for jdx in range(idx + 1, len(hours)):
                if (hours[idx] + hours[jdx]) % 24 == 0:
                    out += 1

        return out
