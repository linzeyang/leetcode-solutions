"""1636. Sort Array by Increasing Frequency"""

from collections import Counter
from functools import cmp_to_key
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        self.cc = Counter(nums)

        out = []

        for key in sorted(self.cc.keys(), key=cmp_to_key(self._cmp_func)):
            out.extend([key] * self.cc[key])

        return out

    def _cmp_func(self, a: int, b: int) -> int:
        if self.cc[a] < self.cc[b]:
            return -1

        if self.cc[a] > self.cc[b]:
            return 1

        if a > b:
            return -1

        if a < b:
            return 1

        return 0
