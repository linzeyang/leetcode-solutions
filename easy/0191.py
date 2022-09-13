"""
191. Number of 1 Bits
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        # Runtime: 32 ms, faster than 93.35% of Python3 online submissions for Number of 1 Bits.
        # Memory Usage: 14 MB, less than 8.00% of Python3 online submissions for Number of 1 Bits.
        return bin(n).count("1")
