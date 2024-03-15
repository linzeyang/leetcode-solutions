"""238. Product of Array Except Self"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out: list[int] = [1] * len(nums)

        prefix = 1

        for idx, num in enumerate(nums):
            out[idx] = prefix
            prefix *= num

        postfix = 1

        for jdx in range(1, len(nums) + 1):
            out[-jdx] *= postfix
            postfix *= nums[-jdx]

        return out
