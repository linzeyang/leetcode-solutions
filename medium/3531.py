"""3531. Count Covered Buildings"""

from typing import List


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        y_range_per_x: dict[int, list[int]] = {}
        x_range_per_y: dict[int, list[int]] = {}

        for x, y in buildings:
            if x not in y_range_per_x:
                y_range_per_x[x] = [y, y]
            else:
                if y < y_range_per_x[x][0]:
                    y_range_per_x[x][0] = y
                elif y > y_range_per_x[x][1]:
                    y_range_per_x[x][1] = y

            if y not in x_range_per_y:
                x_range_per_y[y] = [x, x]
            else:
                if x < x_range_per_y[y][0]:
                    x_range_per_y[y][0] = x
                elif x > x_range_per_y[y][1]:
                    x_range_per_y[y][1] = x

        out = 0

        for x, y in buildings:
            if (
                x not in y_range_per_x
                or y <= y_range_per_x[x][0]
                or y >= y_range_per_x[x][1]
                or y not in x_range_per_y
                or x <= x_range_per_y[y][0]
                or x >= x_range_per_y[y][1]
            ):
                continue

            out += 1

        return out
