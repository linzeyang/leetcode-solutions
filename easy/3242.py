"""3242. Design Neighbor Sum Service"""

from typing import List


class NeighborSum:
    def __init__(self, grid: List[List[int]]):
        self._grid = grid
        self._mapping = {}
        self._n = len(grid)

        for i in range(self._n):
            for j in range(self._n):
                self._mapping[grid[i][j]] = (i, j)

    def adjacentSum(self, value: int) -> int:
        row, col = self._mapping[value]

        if row == 0:
            up = 0
        else:
            up = self._grid[row - 1][col]

        if row == self._n - 1:
            down = 0
        else:
            down = self._grid[row + 1][col]

        if col == 0:
            left = 0
        else:
            left = self._grid[row][col - 1]

        if col == self._n - 1:
            right = 0
        else:
            right = self._grid[row][col + 1]

        return up + down + left + right

    def diagonalSum(self, value: int) -> int:
        row, col = self._mapping[value]

        row_pos1, col_pos1 = row - 1, col - 1

        if (
            row_pos1 < 0
            or row_pos1 > self._n - 1
            or col_pos1 < 0
            or col_pos1 > self._n - 1
        ):
            val1 = 0
        else:
            val1 = self._grid[row_pos1][col_pos1]

        row_pos2, col_pos2 = row - 1, col + 1

        if (
            row_pos2 < 0
            or row_pos2 > self._n - 1
            or col_pos2 < 0
            or col_pos2 > self._n - 1
        ):
            val2 = 0
        else:
            val2 = self._grid[row_pos2][col_pos2]

        row_pos3, col_pos3 = row + 1, col - 1

        if (
            row_pos3 < 0
            or row_pos3 > self._n - 1
            or col_pos3 < 0
            or col_pos3 > self._n - 1
        ):
            val3 = 0
        else:
            val3 = self._grid[row_pos3][col_pos3]

        row_pos4, col_pos4 = row + 1, col + 1

        if (
            row_pos4 < 0
            or row_pos4 > self._n - 1
            or col_pos4 < 0
            or col_pos4 > self._n - 1
        ):
            val4 = 0
        else:
            val4 = self._grid[row_pos4][col_pos4]

        return val1 + val2 + val3 + val4


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
