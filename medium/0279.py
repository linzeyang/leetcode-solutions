"""279. Perfect Squares"""

from functools import cache


class Solution:
    @cache
    def numSquares(self, n: int) -> int:
        min_num = None
        pivot = int(n**0.5)

        if pivot**2 == n:
            return 1

        while pivot:
            count = 1 + self.numSquares(n - pivot**2)

            if not min_num or count < min_num:
                min_num = count

            pivot -= 1

        return min_num
