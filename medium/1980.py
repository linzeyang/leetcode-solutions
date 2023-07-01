"""1980. Find Unique Binary String"""

from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        length = len(nums)

        for num in range(2**length):
            if (st := f"{num:0>{length}b}") not in nums:
                return st
