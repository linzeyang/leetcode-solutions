"""2951. Find the Peaks"""

from typing import List


class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        return [
            idx
            for idx in range(1, len(mountain) - 1)
            if mountain[idx - 1] < mountain[idx] and mountain[idx] > mountain[idx + 1]
        ]
