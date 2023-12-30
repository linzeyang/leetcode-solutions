"""79. Word Search"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        starts: list[tuple[int, int]] = []

        chars = set()

        for idx, row in enumerate(board):
            for jdx, char in enumerate(row):
                chars.add(char)
                if char == word[0]:
                    starts.append((idx, jdx))

        if not set(word).issubset(chars):
            return False

        if not starts:
            return False

        if len(word) == 1:
            return True

        for idx, jdx in starts:
            if self._backtrack(board, word, [(idx, jdx)]):
                return True

        return False

    def _backtrack(
        self, board: list[list[str]], word: str, path: list[tuple[int, int]]
    ) -> bool:
        if len(path) == len(word):
            return True

        char = word[len(path)]
        y, x = path[-1]

        for delta_y, delta_x in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            new_y, new_x = y + delta_y, x + delta_x

            if (
                new_y < 0
                or new_y >= len(board)
                or new_x < 0
                or new_x >= len(board[0])
                or (new_y, new_x) in path
            ):
                continue

            if board[new_y][new_x] == char:
                path.append((new_y, new_x))

                if self._backtrack(board, word, path):
                    return True

                path.pop()

        return False
