"""1582. Special Positions in a Binary Matrix"""

from typing import List


class Solution:
    """
    https://leetcode.com/problems/special-positions-in-a-binary-matrix/
    Weekly Contest 206
    """

    def numSpecial(self, mat: List[List[int]]) -> int:
        by_row: dict[int, set[int]] = {}
        by_col: dict[int, set[int]] = {}

        for idx, row in enumerate(mat):
            for jdx, num in enumerate(row):
                if num == 1:
                    by_row.setdefault(idx, set()).add(jdx)
                    by_col.setdefault(jdx, set()).add(idx)

        out: int = 0

        for columns in by_row.values():
            if len(columns) == 1 and len(by_col[next(iter(columns))]) == 1:
                out += 1

        return out
