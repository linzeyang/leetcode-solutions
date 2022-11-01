"""1281. Subtract the Product and Sum of Digits of an Integer"""

from math import prod


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = [int(num) for num in str(n)]

        return prod(s) - sum(s)
