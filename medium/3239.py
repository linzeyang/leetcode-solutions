"""3239. Minimum Number of Flips to Make Binary Grid Palindromic I"""

from typing import List


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        count_horizontal = 0

        for row in grid:
            left, right = 0, len(row) - 1

            while left < right:
                if row[left] != row[right]:
                    count_horizontal += 1

                left += 1
                right -= 1

        count_vertical = 0

        for column_idx in range(len(grid[0])):
            up, down = 0, len(grid) - 1

            while up < down:
                if grid[up][column_idx] != grid[down][column_idx]:
                    count_vertical += 1

                up += 1
                down -= 1

        return min(count_horizontal, count_vertical)
