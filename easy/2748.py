"""2748. Number of Beautiful Pairs"""

from itertools import combinations
from typing import List


class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        return sum(
            1
            for tup1, tup2 in combinations((self._decompose(num) for num in nums), 2)
            if self._gcd(tup1[0], tup2[1]) == 1
        )

    def _decompose(self, num: int) -> tuple[int, int]:
        if num < 10:
            return num, num

        return int(str(num)[0]), num % 10

    def _gcd(self, num1: int, num2: int) -> int:
        if num1 == 1 or num2 == 1:
            return 1

        if num1 < num2:
            num1, num2 = num2, num1

        while num1 % num2:
            num1, num2 = num2, num1 - num2

            if num1 < num2:
                num1, num2 = num2, num1

        return num2
