"""1018. Binary Prefix Divisible By 5"""

from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        out = []
        number = 0

        for num in nums:
            number = 2 * number + num
            out.append(number % 5 == 0)

        return out
