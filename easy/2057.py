"""2057. Smallest Index With Equal Value"""

from typing import List


class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for idx, n in enumerate(nums):
            if idx % 10 == n:
                return idx

        return -1
