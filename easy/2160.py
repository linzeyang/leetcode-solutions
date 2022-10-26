"""2160. Minimum Sum of Four Digit Number After Splitting Digits"""


class Solution:
    def minimumSum(self, num: int) -> int:
        a, b, c, d = sorted(str(num))

        return int(f"{a}{c}") + int(f"{b}{d}")
