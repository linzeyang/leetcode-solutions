"""3804. Number of Centered Subarrays"""

from typing import List


class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        out: int = len(nums)

        for idx in range(len(nums) - 1):
            sub_sum: int = nums[idx]
            sub_set: set[int] = {nums[idx]}

            for jdx in range(idx + 1, len(nums)):
                sub_sum += nums[jdx]
                sub_set.add(nums[jdx])

                if sub_sum in sub_set:
                    out += 1

        return out
