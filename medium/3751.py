"""3751. Total Waviness of Numbers in Range I"""


class Solution:
    """
    https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/
    Biweekly Contest 170
    """

    def totalWaviness(self, num1: int, num2: int) -> int:
        if num2 < 101:
            return 0

        num1: int = max(num1, 101)

        out: int = 0

        for num in range(num1, num2 + 1):
            s: str = str(num)
            waviness: int = 0

            for i in range(1, len(s) - 1):
                left: str = s[i - 1]
                mid: str = s[i]
                right: str = s[i + 1]

                if (left < mid and mid > right) or (left > mid and mid < right):
                    waviness += 1

            out += waviness

        return out
