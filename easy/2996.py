"""2996. Smallest Missing Integer Greater Than Sequential Prefix Sum"""

from typing import List


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0] + 1

        nums_set: set[int] = set(nums)

        out = nums[0]

        for idx in range(1, len(nums)):
            if nums[idx] - nums[idx - 1] == 1:
                out += nums[idx]
            else:
                break

        while out in nums_set:
            out += 1

        return out
