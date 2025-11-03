"""3723. Maximize Sum of Squares of Digits"""


class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        """
        To maximize the sum of squares, we should use as many 9's as possible.
        If the sum is divisible by 9, we can use all 9's.
        If the sum is not divisible by 9, we can use (sum % 9) as the last digit.
        """

        # If the sum is greater than num * 9,
        # it's impossible to form a number with num digits.
        if sum > num * 9:
            return ""

        div, mod = divmod(sum, 9)

        return f"{'9' * div}{mod:0<{num - div}}" if num - div else f"{'9' * div}"
