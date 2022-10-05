"""455. Assign Cookies"""

from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        count = 0
        idx = 0
        length = len(g)

        for coo in s:
            if idx < length:
                if coo >= g[idx]:
                    count += 1
                    idx += 1
            else:
                break

        return count
