"""2109. Adding Spaces to a String"""

from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        out: list[str] = []

        jdx = 0

        for idx, char in enumerate(s):
            if jdx < len(spaces) and idx == spaces[jdx]:
                out.append(" ")
                jdx += 1

            out.append(char)

        return "".join(out)
