"""1480. Running Sum of 1d Array"""

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        out = []

        for num in nums:
            total += num
            out.append(total)

        return out
