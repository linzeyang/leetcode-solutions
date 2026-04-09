"""
3653. XOR After Range Multiplication Queries I

https://leetcode.com/problems/xor-after-range-multiplication-queries-i/

Weekly Contest 463
"""

from functools import reduce
from typing import List


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod: int = 1_000_000_000 + 7

        for left, right, k, v in queries:
            idx: int = left

            while idx <= right:
                nums[idx] = (nums[idx] * v) % mod
                idx += k

        return reduce(lambda x, y: x ^ y, nums)
