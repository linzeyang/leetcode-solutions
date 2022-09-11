"""
136. Single Number
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Runtime: 246 ms, faster than 39.56% of Python3 online submissions for Single Number.
        # Memory Usage: 17.2 MB, less than 5.11% of Python3 online submissions for Single Number.
        store = set()

        for n in nums:
            if n not in store:
                store.add(n)
            else:
                store.remove(n)

        for n in store:
            return n
