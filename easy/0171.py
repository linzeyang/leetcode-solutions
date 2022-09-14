"""
171. Excel Sheet Column Number
"""
from string import ascii_uppercase

TEMP = dict(zip(ascii_uppercase, range(1, 27)))


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # Very slow:
        # Runtime: 72 ms, faster than 9.57% of Python3 online submissions for Excel Sheet Column Number.
        # Memory Usage: 13.9 MB, less than 56.18% of Python3 online submissions for Excel Sheet Column Number.
        return sum(
            TEMP[columnTitle[-i]] * 26 ** (i - 1)
            for i in range(1, len(columnTitle) + 1)
        )
