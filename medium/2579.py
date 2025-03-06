"""2579. Count Total Number of Colored Cells"""


class Solution:
    def coloredCells(self, n: int) -> int:
        # Except for the 1st second, the number of additional cells at each second
        # is an arithmetic progression with common difference of 4: 4, 8, 12.
        # thus the sum of all cells at nth second is:
        # 1 + (0 + (n - 1) x 4) x n / 2
        # which is equivalent to:

        return 2 * n**2 - 2 * n + 1
