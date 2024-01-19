"""2164. Sort Even and Odd Indices Independently"""

from typing import List


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        if len(nums) < 3:
            return nums

        evens = sorted(nums[::2])
        odds = sorted(nums[1::2], reverse=True)

        out = []

        for a, b in zip(evens, odds, strict=False):
            out.append(a)
            out.append(b)

        if len(evens) > len(odds):
            out.append(evens[-1])

        return out
