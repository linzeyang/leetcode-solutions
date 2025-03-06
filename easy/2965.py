"""2965. Find Missing and Repeated Values"""

from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        missing = repeated = 0

        counter: list[int] = [0] * len(grid) ** 2

        for row in grid:
            for num in row:
                counter[num - 1] += 1

                if not repeated and counter[num - 1] == 2:
                    repeated = num

        for idx, num in enumerate(counter):
            if num == 0:
                missing = idx + 1
                break

        return [repeated, missing]
