"""3190. Find Minimum Operations to Make All Elements Divisible by Three"""

from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(1 for num in nums if num % 3)
