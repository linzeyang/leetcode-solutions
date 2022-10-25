"""1863. Sum of All Subset XOR Totals"""

from functools import reduce
from itertools import combinations
from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return sum(nums) + sum(
            sum(reduce(lambda x, y: x ^ y, comb) for comb in combinations(nums, i))
            for i in range(2, len(nums) + 1)
        )
