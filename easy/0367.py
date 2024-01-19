"""367. Valid Perfect Square"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return num**0.5 % 1 == 0
