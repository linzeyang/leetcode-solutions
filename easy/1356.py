"""1356. Sort Integers by The Number of 1 Bits"""

from typing import List


class Solution:
    """
    https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
    Biweekly Contest 20
    """

    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda num: (bin(num).count("1"), num))
