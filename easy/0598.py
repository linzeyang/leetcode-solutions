"""598. Range Addition II"""

from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        x, y = m, n

        for a, b in ops:
            x = min(x, a)
            y = min(y, b)

        return x * y
