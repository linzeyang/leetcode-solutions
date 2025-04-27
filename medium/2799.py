"""2799. Count Complete Subarrays in an Array"""

from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        num_of_unique = len(set(nums))

        out = 0

        for idx in range(len(nums)):
            current: set[int] = set()

            for jdx in range(idx, len(nums)):
                current.add(nums[jdx])

                if len(current) == num_of_unique:
                    out += len(nums) - jdx
                    break
            else:
                break

        return out
