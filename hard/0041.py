"""41. First Missing Positive"""

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        i = 1

        while i in nums_set:
            i += 1

        return i
