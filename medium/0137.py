"""137. Single Number II"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sin = set()
        mul = set()

        for num in nums:
            if num not in mul:
                if num not in sin:
                    sin.add(num)
                else:
                    sin.remove(num)
                    mul.add(num)

        return next(iter(sin))
