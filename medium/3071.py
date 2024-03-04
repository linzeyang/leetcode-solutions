"""3071. Minimum Operations to Write the Letter Y on a Grid"""

from typing import List


class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        mapping: dict[int, int] = {
            0: 0,
            1: 0,
            2: 0,
        }

        mapping_2: dict[int, int] = {
            0: 0,
            1: 0,
            2: 0,
        }

        for idx in range(len(grid) // 2):
            for jdx in range(len(grid)):
                if jdx in (idx, len(grid) - idx - 1):
                    mapping[grid[idx][jdx]] += 1
                else:
                    mapping_2[grid[idx][jdx]] += 1

        for idx in range(len(grid) // 2, len(grid)):
            for jdx in range(len(grid)):
                if jdx == len(grid) // 2:
                    mapping[grid[idx][jdx]] += 1
                else:
                    mapping_2[grid[idx][jdx]] += 1

        return min(
            mapping[1] + mapping[2] + mapping_2[0] + mapping_2[2],
            mapping[1] + mapping[2] + mapping_2[0] + mapping_2[1],
            mapping[0] + mapping[2] + mapping_2[1] + mapping_2[2],
            mapping[0] + mapping[2] + mapping_2[0] + mapping_2[1],
            mapping[0] + mapping[1] + mapping_2[1] + mapping_2[2],
            mapping[0] + mapping[1] + mapping_2[0] + mapping_2[2],
        )
