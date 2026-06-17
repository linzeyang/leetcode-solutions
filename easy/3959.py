"""
3959. Check Good Integer

https://leetcode.com/problems/check-good-integer/

Weekly Contest 506
"""


class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digits: list[int] = [int(char) for char in str(n)]

        return sum(d**2 for d in digits) - sum(digits) >= 50
