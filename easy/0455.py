"""455. Assign Cookies"""

from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        idx = jdx = out = 0

        while idx < len(g) and jdx < len(s):
            if s[jdx] >= g[idx]:
                out += 1
                idx += 1
            jdx += 1

        return out
