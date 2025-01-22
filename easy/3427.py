"""3427. Sum of Variable Length Subarrays"""

from typing import List


class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        out = 0

        for idx, num in enumerate(nums):
            start = max(0, idx - num)

            out += sum(nums[start : idx + 1])

        return out
