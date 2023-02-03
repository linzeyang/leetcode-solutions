"""1313. Decompress Run-Length Encoded List"""

from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        out = []

        for idx in range(len(nums) // 2):
            out += [nums[idx * 2 + 1]] * nums[idx * 2]

        return out
