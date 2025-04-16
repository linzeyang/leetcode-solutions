"""2869. Minimum Operations to Collect Elements"""

from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        out = 0
        collection: set[int] = set()

        while len(collection) < k:
            num = nums.pop()
            out += 1

            if num <= k:
                collection.add(num)

        return out
