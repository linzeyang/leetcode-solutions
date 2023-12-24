"""137. Single Number II"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = {}

        for num in nums:
            if num not in temp:
                temp[num] = 1
            elif temp[num] == 1:
                temp[num] = 2
            else:
                del temp[num]

        return next(iter(temp.keys()))
