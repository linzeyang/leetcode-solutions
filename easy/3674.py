"""3674. Minimum Operations to Equalize Array"""

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        length: int = len(nums)

        if length == 1:
            return 0

        pivot: int = nums[0]

        if all(nums[idx] == pivot for idx in range(1, length)):
            return 0

        return 1
