"""3402. Minimum Operations to Make Columns Strictly Increasing"""

from typing import List


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        len_i = len(grid)
        len_j = len(grid[0])

        if len_i == 1:
            return 0

        out = 0

        targets = [num + 1 for num in grid[0]]

        for i in range(1, len_i):
            for j in range(len_j):
                if grid[i][j] > targets[j]:
                    targets[j] = grid[i][j] + 1
                else:
                    out += targets[j] - grid[i][j]
                    targets[j] += 1

        return out
