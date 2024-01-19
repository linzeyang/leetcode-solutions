"""171. Excel Sheet Column Number"""

from string import ascii_uppercase

TEMP = dict(zip(ascii_uppercase, range(1, 27), strict=False))


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        return sum(
            TEMP[columnTitle[-i]] * 26 ** (i - 1)
            for i in range(1, len(columnTitle) + 1)
        )
