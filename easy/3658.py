"""
3658. GCD of Odd and Even Sums

https://leetcode.com/problems/gcd-of-odd-and-even-sums/

Weekly Contest 464
"""

from math import gcd


class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sum_odd: int = n**2
        sum_even: int = sum_odd + n

        return gcd(sum_odd, sum_even)
