"""2965. Find Missing and Repeated Values"""

from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        temp: list[int] = [0] * len(grid) ** 2

        for row in grid:
            for num in row:
                temp[num - 1] += 1

        out = [0, 0]

        for idx, num in enumerate(temp):
            if num == 2:
                out[0] = idx + 1
            elif num == 0:
                out[1] = idx + 1

            if all(out):
                break

        return out
