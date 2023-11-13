"""36. Valid Sudoku"""

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows: dict[int, set[str]] = {}
        columns: dict[int, set[str]] = {}
        blocks: dict[int, dict[int, set[str]]] = {}

        for idx, row in enumerate(board):
            for jdx, num in enumerate(row):
                if num == ".":
                    continue

                if idx not in rows:
                    rows[idx] = {num}
                elif num not in rows[idx]:
                    rows[idx].add(num)
                else:
                    return False

                if jdx not in columns:
                    columns[jdx] = {num}
                elif num not in columns[jdx]:
                    columns[jdx].add(num)
                else:
                    return False

                if idx // 3 not in blocks:
                    blocks[idx // 3] = {jdx // 3: {num}}
                elif jdx // 3 not in blocks[idx // 3]:
                    blocks[idx // 3][jdx // 3] = {num}
                elif num not in blocks[idx // 3][jdx // 3]:
                    blocks[idx // 3][jdx // 3].add(num)
                else:
                    return False

        return True
