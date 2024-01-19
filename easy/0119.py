"""119. Pascal's Triangle II"""

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        out = []

        for j in range(rowIndex + 1):
            if not out:
                out.append(1)
            else:
                new = []
                for i in range(j + 1):
                    if i == 0 or i == j:
                        new.append(1)
                    else:
                        new.append(out[i - 1] + out[i])
                out = new
        return out
