"""130. Surrounded Regions"""

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        grids_not_to_flood: list[tuple[int, int]] = []

        for idx, row in enumerate(board):
            for jdx, node in enumerate(row):
                if node == "O":
                    grids, not_to_flood = self._find_to_flood(
                        board, idx, jdx, grids_not_to_flood
                    )
                    if not_to_flood:
                        grids_not_to_flood.extend(grids)

        for grid in grids_not_to_flood:
            board[grid[0]][grid[1]] = "O"

    def _find_to_flood(
        self,
        board: list[list[str]],
        idx: int,
        jdx: int,
        grids_not_to_flood: list[tuple[int, int]],
    ) -> tuple[list[tuple[int, int]], bool]:
        board[idx][jdx] = "X"

        local_grids = [(idx, jdx)]

        res = idx in (0, len(board) - 1) or jdx in (0, len(board[0]) - 1)

        if idx >= 1 and board[idx - 1][jdx] == "O":
            grids1, res1 = self._find_to_flood(board, idx - 1, jdx, grids_not_to_flood)
            local_grids += grids1
            res = res or res1
        if idx < len(board) - 1 and board[idx + 1][jdx] == "O":
            grids2, res2 = self._find_to_flood(board, idx + 1, jdx, grids_not_to_flood)
            local_grids += grids2
            res = res or res2
        if jdx >= 1 and board[idx][jdx - 1] == "O":
            grids3, res3 = self._find_to_flood(board, idx, jdx - 1, grids_not_to_flood)
            local_grids += grids3
            res = res or res3
        if jdx < len(board[0]) - 1 and board[idx][jdx + 1] == "O":
            grids4, res4 = self._find_to_flood(board, idx, jdx + 1, grids_not_to_flood)
            local_grids += grids4
            res = res or res4

        return local_grids, res
