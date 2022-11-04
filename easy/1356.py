"""1356. Sort Integers by The Number of 1 Bits"""

from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(sorted(arr), key=lambda num: bin(num).count("1"))
