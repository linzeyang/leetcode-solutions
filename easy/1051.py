"""1051. Height Checker"""

from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        ll = sorted(heights)

        for idx, num in enumerate(heights):
            if num != ll[idx]:
                count += 1

        return count
