"""944. Delete Columns to Make Sorted"""

from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        out: int = 0

        for col in range(len(strs[0])):
            for row in range(1, len(strs)):
                if strs[row][col] < strs[row - 1][col]:
                    out += 1
                    break

        return out
