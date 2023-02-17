"""2022. Convert 1D Array Into 2D Array"""

from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []

        if m == 1 == n:
            return [original]

        return [original[n * idx: n * (idx + 1)] for idx in range(m)]
