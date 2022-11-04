"""1374. Generate a String With Characters That Have Odd Counts"""


class Solution:
    def generateTheString(self, n: int) -> str:
        if n == 1:
            return "a"
        if n == 2:
            return "ab"

        if n % 2 == 0:
            half = n // 2
            z = 0
        else:
            half = (n - 1) // 2
            z = 1

        if half % 2 == 1:
            x = y = half
        else:
            x, y = half - 1, half + 1

        return "a" * x + "b" * y + "c" * z
