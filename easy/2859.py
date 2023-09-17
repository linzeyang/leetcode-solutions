"""2859. Sum of Values at Indices With K Set Bits"""

from typing import List


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        return sum(num for idx, num in enumerate(nums) if self._set_bits(idx) == k)

    @staticmethod
    def _set_bits(num: int) -> int:
        return bin(num).count("1")
