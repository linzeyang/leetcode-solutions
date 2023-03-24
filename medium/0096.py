"""96. Unique Binary Search Trees"""

from functools import lru_cache


class Solution:
    @lru_cache(maxsize=20, typed=True)
    def numTrees(self, n: int) -> int:
        if n < 2:
            return 1

        if n == 2:
            return 2

        return sum(self.numTrees(i) * self.numTrees(n - i - 1) for i in range(n))
