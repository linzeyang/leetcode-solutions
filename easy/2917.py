"""2917. Find the K-or of an Array"""

from typing import List


class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        num_bits = len(f"{max(nums):b}")
        out = 0

        for bit in range(num_bits + 1):
            bit_2 = 2**bit
            count = sum(1 for num in nums if (bit_2 & num) == bit_2)

            if count >= k:
                out += bit_2

        return out
