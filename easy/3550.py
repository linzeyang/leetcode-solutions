"""3550. Smallest Index With Digit Sum Equal to Index"""

from typing import List


class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for idx, num in enumerate(nums):
            if idx == sum(int(char) for char in str(num)):
                return idx

        return -1
