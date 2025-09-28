"""3688. Bitwise OR of Even Numbers in an Array"""

from typing import List


class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        out: int = 0

        for num in nums:
            if not num & 1:
                out |= num

        return out
