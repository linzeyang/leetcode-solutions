"""
3908. Valid Digit Number

https://leetcode.com/problems/valid-digit-number/

Biweekly Contest 181
"""


class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        str_n: str = str(n)
        str_x: str = str(x)

        return str_x in str_n and not str_n.startswith(str_x)
