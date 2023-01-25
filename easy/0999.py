"""999. Available Captures for Rook"""

from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        r_y = r_x = 0

        for idx, row in enumerate(board):
            if "R" in row:
                r_y = idx
                r_x = row.index("R")
                break

        out = 0

        if r_x < 7:
            for idx in range(r_x + 1, 8):
                if board[r_y][idx] == "p":
                    out += 1
                    break

                if board[r_y][idx] == "B":
                    break

        if r_x > 0:
            for idx in range(r_x - 1, -1, -1):
                if board[r_y][idx] == "p":
                    out += 1
                    break

                if board[r_y][idx] == "B":
                    break

        if r_y < 7:
            for idx in range(r_y + 1, 8):
                if board[idx][r_x] == "p":
                    out += 1
                    break

                if board[idx][r_x] == "B":
                    break

        if r_y > 0:
            for idx in range(r_y - 1, -1, -1):
                if board[idx][r_x] == "p":
                    out += 1
                    break

                if board[idx][r_x] == "B":
                    break

        return out
