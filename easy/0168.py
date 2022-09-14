"""
168. Excel Sheet Column Title
"""

from string import ascii_uppercase

TEMP = dict(zip(range(26), ascii_uppercase))


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # Slow:
        # Runtime: 57 ms, faster than 22.50% of Python3 online submissions for Excel Sheet Column Title.
        # Memory Usage: 13.8 MB, less than 96.64% of Python3 online submissions for Excel Sheet Column Title.
        out = ""

        while columnNumber > 0:
            columnNumber -= 1
            out = TEMP[columnNumber % 26] + out

            columnNumber //= 26

        return out
