"""
3954. Sum of Compatible Numbers in Range I

https://leetcode.com/problems/sum-of-compatible-numbers-in-range-i/

Weekly Contest 505
"""


class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        return sum(x for x in range(max(n - k, 0), n + k + 1) if n & x == 0)
