"""260. Single Number III"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        temp: set[int] = set()

        for num in nums:
            if num not in temp:
                temp.add(num)
            else:
                temp.remove(num)

        return list(temp)
