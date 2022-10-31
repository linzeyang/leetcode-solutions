"""1827. Minimum Operations to Make the Array Increasing"""

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        out = 0

        for i in range(1, len(nums)):
            cur = nums[i]

            pre = nums[i - 1]

            if cur <= pre:
                should_be = pre + 1
                out += should_be - cur
                nums[i] = should_be

        return out
