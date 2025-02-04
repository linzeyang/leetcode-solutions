"""2148. Count Elements With Strictly Smaller and Greater Elements"""

from typing import List


class Solution:
    def countElements(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        temp = {min(nums), max(nums)}
        out = 0

        for num in nums:
            if num not in temp:
                out += 1

        return out
