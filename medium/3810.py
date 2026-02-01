"""3810. Minimum Operations to Reach Target Array"""

from typing import List


class Solution:
    """
    https://leetcode.com/problems/minimum-operations-to-reach-target-array/
    Biweekly Contest 174
    """

    def minOperations(self, nums: List[int], target: List[int]) -> int:
        return len({num for num, tar in zip(nums, target, strict=True) if num != tar})
