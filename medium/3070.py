"""3070. Count Submatrices with Top-Left Element and Sum Less Than k"""

from typing import List


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        if grid[0][0] > k:
            return 0

        sums: list[list[int]] = [[0] * len(grid[0]) for _ in range(len(grid))]
        sums[0][0] = grid[0][0]
        out = 1

        for idx in range(1, len(grid[0])):
            sub_sum = grid[0][idx] + sums[0][idx - 1]

            if sub_sum > k:
                sums[0][idx] = -1
                break

            sums[0][idx] = sub_sum
            out += 1

        for idx in range(1, len(grid)):
            row_sum = 0

            for jdx in range(len(grid[0])):
                if sums[idx - 1][jdx] == -1:
                    sums[idx][jdx] = -1
                    break

                row_sum += grid[idx][jdx]

                if jdx == 0:
                    sub_sum = grid[idx][jdx] + sums[idx - 1][jdx]
                else:
                    sub_sum = row_sum + sums[idx - 1][jdx]

                if sub_sum > k:
                    sums[idx][jdx] = -1
                    break

                sums[idx][jdx] = sub_sum
                out += 1

        return out
