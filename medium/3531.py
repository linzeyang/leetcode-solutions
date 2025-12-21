"""3531. Count Covered Buildings"""

from typing import List


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        x_ranges: dict[int, list[int]] = {}
        y_ranges: dict[int, list[int]] = {}

        for x, y in buildings:
            if y not in x_ranges:
                x_ranges[y] = [x, x]
            else:
                x_ranges[y] = [min(x, x_ranges[y][0]), max(x, x_ranges[y][1])]

            if x not in y_ranges:
                y_ranges[x] = [y, y]
            else:
                y_ranges[x] = [min(y, y_ranges[x][0]), max(y, y_ranges[x][1])]

        out: int = 0

        for x, y in buildings:
            if (
                y_ranges[x][0] < y < y_ranges[x][1]
                and x_ranges[y][0] < x < x_ranges[y][1]
            ):
                out += 1

        return out
