"""2661. First Completely Painted Row or Column"""

from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        mapping: dict[int, tuple[int, int]] = {}

        for idx, row in enumerate(mat):
            for jdx, num in enumerate(row):
                mapping[num] = (idx, jdx)

        rows: list[int] = [0] * len(mat)
        cols: list[int] = [0] * len(mat[0])

        out = -1

        for adx, digit in enumerate(arr):
            ro, co = mapping[digit]

            if (rows[ro] == len(mat[0]) - 1) or (cols[co] == len(mat) - 1):
                out = adx
                break

            rows[ro] += 1
            cols[co] += 1

        return out
