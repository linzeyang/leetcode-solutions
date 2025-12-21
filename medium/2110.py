"""2110. Number of Smooth Descent Periods of a Stock"""

from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        length: int = len(prices)

        if length == 1:
            return 1

        out: int = 0
        current: int = 1

        for idx in range(1, length):
            if prices[idx] - prices[idx - 1] == -1:
                current += 1
            else:
                out += (1 + current) * current // 2
                current = 1

        out += (1 + current) * current // 2

        return out
