"""3417. Zigzag Grid Traversal With Skip"""

from typing import List


class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        out: list[int] = []

        odd: bool = len(grid[0]) & 1 == 1

        for idx, row in enumerate(grid):
            if idx & 1 == 0:
                out.extend(row[::2])
            elif odd:
                out.extend(row[-2::-2])
            else:
                out.extend(row[-1::-2])

        return out
