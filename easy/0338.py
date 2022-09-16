"""
338. Counting Bits
"""
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # Runtime: 162 ms, faster than 46.08% of Python3 online submissions for Counting Bits.
        # Memory Usage: 20.8 MB, less than 30.04% of Python3 online submissions for Counting Bits.
        return [bin(i).count("1") for i in range(n + 1)]
