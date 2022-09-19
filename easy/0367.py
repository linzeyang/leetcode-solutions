"""
367. Valid Perfect Square
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Runtime: 54 ms, faster than 42.87% of Python3 online submissions for Valid Perfect Square.
        # Memory Usage: 13.9 MB, less than 10.42% of Python3 online submissions for Valid Perfect Square.

        return num**0.5 % 1 == 0
