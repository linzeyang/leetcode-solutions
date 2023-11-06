"""2923. Find Champion I"""

from typing import List


class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        for idx, row in enumerate(grid):
            if row.count(0) == 1:
                return idx

        return -1
