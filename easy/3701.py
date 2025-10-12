"""3701. Compute Alternating Sum"""

from typing import List


class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        out: int = 0
        sign: int = 1

        for num in nums:
            out += sign * num
            sign *= -1

        return out
