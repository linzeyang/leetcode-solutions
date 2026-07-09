"""
3754. Concatenate Non-Zero Digits and Multiply by Sum I

https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/

Weekly Contest 477
"""


class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if not n:
            return 0

        x: int = 0
        summ: int = 0

        for char in str(n):
            if char == "0":
                continue

            x = x * 10 + int(char)
            summ += int(char)

        return x * summ
