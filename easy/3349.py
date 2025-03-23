"""3349. Adjacent Increasing Subarrays Detection I"""

from typing import List


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        for idx in range(len(nums) - 2 * k + 1):
            for jdx in range(idx + 1, idx + k):
                if nums[jdx] <= nums[jdx - 1]:
                    break
            else:
                for jdx in range(idx + k + 1, idx + 2 * k):
                    if nums[jdx] <= nums[jdx - 1]:
                        break
                else:
                    return True

        return False
