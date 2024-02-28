"""2120. Execution of All Suffix Instructions Staying in a Grid"""

from typing import List


class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        out: list[int] = []

        for idx in range(len(s)):
            steps = 0

            cur_row, cur_col = startPos

            for jdx in range(idx, len(s)):
                match s[jdx]:
                    case "L":
                        cur_col -= 1
                    case "R":
                        cur_col += 1
                    case "U":
                        cur_row -= 1
                    case "D":
                        cur_row += 1

                if cur_row < 0 or cur_row >= n or cur_col < 0 or cur_col >= n:
                    break

                steps += 1

            out.append(steps)

        return out
