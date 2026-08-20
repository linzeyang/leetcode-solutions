"""
3702. Longest Subsequence With Non-Zero Bitwise XOR

https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/

Weekly Contest 470
"""

from functools import reduce
from typing import List


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1 if nums[0] != 0 else 0

        all_xor: int = reduce(lambda a, b: a ^ b, nums)

        if all_xor != 0:
            return len(nums)

        if all(num == 0 for num in nums):
            return 0

        return len(nums) - 1
