"""1304. Find N Unique Integers Sum up to Zero"""

from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]

        if n % 2 == 0:
            return [num for num in range(-n // 2, n // 2 + 1) if num != 0]

        return list(range(-n // 2 + 1, n // 2 + 1))
