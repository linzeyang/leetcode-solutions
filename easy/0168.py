"""168. Excel Sheet Column Title"""

from string import ascii_uppercase

TEMP = dict(zip(range(26), ascii_uppercase, strict=False))


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        out = ""

        while columnNumber > 0:
            columnNumber -= 1
            out = TEMP[columnNumber % 26] + out

            columnNumber //= 26

        return out
