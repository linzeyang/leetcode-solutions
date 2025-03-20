"""2614. Prime In Diagonal"""

from functools import lru_cache
from typing import List


class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        out = 0

        for idx in range(len(nums)):
            if self._is_prime(nums[idx][idx]):
                out = max(out, nums[idx][idx])

            if self._is_prime(nums[idx][len(nums) - idx - 1]):
                out = max(out, nums[idx][len(nums) - idx - 1])

        return out

    @lru_cache(maxsize=1_000)
    def _is_prime(self, num: int) -> bool:
        if num == 1:
            return False

        if num in (2, 3, 5, 7, 11, 13, 17):
            return True

        if num & 1 == 0:
            return False

        for factor in range(3, int(num**0.5) + 1, 2):
            if num % factor == 0:
                return False

        return True
