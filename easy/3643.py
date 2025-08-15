"""3643. Flip Square Submatrix Vertically"""

from typing import List


class Solution:
    def reverseSubmatrix(
        self, grid: List[List[int]], x: int, y: int, k: int
    ) -> List[List[int]]:
        for i in range(k // 2):
            # Swap row (x + i) and row (x + k - 1 - i) for columns y to y+k-1
            for j in range(k):
                grid[x + i][y + j], grid[x + k - 1 - i][y + j] = (
                    grid[x + k - 1 - i][y + j],
                    grid[x + i][y + j],
                )
        return grid
