"""2932. Maximum Strong Pair XOR I"""

from typing import List


class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        out = 0

        for idx in range(len(nums) - 1):
            for jdx in range(idx + 1, len(nums)):
                if (
                    abs(nums[idx] - nums[jdx]) <= min(nums[idx], nums[jdx])
                    and nums[idx] ^ nums[jdx] > out
                ):
                    out = nums[idx] ^ nums[jdx]

        return out
