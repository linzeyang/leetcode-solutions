"""
190. Reverse Bits
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        # Runtime: 50 ms, faster than 57.48% of Python3 online submissions for Reverse Bits.
        # Memory Usage: 13.8 MB, less than 49.30% of Python3 online submissions for Reverse Bits.
        return int(f"{bin(n)[2:]:0>32}"[::-1], 2)
