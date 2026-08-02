"""
3513. Number of Unique XOR Triplets I

https://leetcode.com/problems/number-of-unique-xor-triplets-i/

Biweekly Contest 154
"""

from typing import List


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        length: int = len(nums)

        if length <= 2:
            return length

        return 2 << (len(bin(length)) - 3)
