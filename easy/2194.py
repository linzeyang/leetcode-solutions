"""2194. Cells in a Range on an Excel Sheet"""

from typing import List


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        col_start, col_stop, row_start, row_stop = s[0], s[3], s[1], s[4]

        return [
            f"{chr(i)}{j}"
            for i in range(ord(col_start), ord(col_stop) + 1)
            for j in range(int(row_start), int(row_stop) + 1)
        ]
