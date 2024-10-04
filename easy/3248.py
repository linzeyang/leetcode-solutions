"""3248. Snake in Matrix"""

from typing import List


class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        row = col = 0

        for comm in commands:
            match comm:
                case "UP":
                    row -= 1
                case "DOWN":
                    row += 1
                case "LEFT":
                    col -= 1
                case "RIGHT":
                    col += 1

        return row * n + col
