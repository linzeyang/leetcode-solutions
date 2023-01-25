"""1030. Matrix Cells in Distance Order"""

from typing import List


class Solution:
    def allCellsDistOrder(
        self, rows: int, cols: int, rCenter: int, cCenter: int
    ) -> List[List[int]]:
        ite = ([x_axis, y_axis] for x_axis in range(rows) for y_axis in range(cols))

        return sorted(
            ite, key=lambda coords: abs(coords[0] - rCenter) + abs(coords[1] - cCenter)
        )
