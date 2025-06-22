"""3591. Check if Any Element Has Prime Frequency"""

from collections import Counter
from typing import List


class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        counter: Counter[int] = Counter(nums)

        for val in counter.values():
            if self._is_prime(val):
                return True

        return False

    def _is_prime(self, num: int) -> bool:
        if num < 2:
            return False

        if num == 2:
            return True

        if num & 1 == 0:
            return False

        for fac in range(3, int(num**0.5) + 1, 2):
            if num % fac == 0:
                return False

        return True
