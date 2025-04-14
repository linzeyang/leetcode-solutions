"""3513. Number of Unique XOR Triplets I"""

from typing import List


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        length = len(nums)

        if length <= 2:
            return length

        return 2 ** (len(bin(length)) - 2)
