"""3576. Transform Array to All Equal Elements"""

from typing import List


class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        nums2: list[int] = nums[:]

        # convert all to 1
        counter = 0

        for idx in range(len(nums) - 1):
            if nums[idx] == -1:
                nums[idx + 1] *= -1
                counter += 1

        if nums[-1] == 1 and counter <= k:
            return True

        # convert all to -1
        counter = 0

        for idx in range(len(nums) - 1):
            if nums2[idx] == 1:
                nums2[idx + 1] *= -1
                counter += 1

        if nums[-1] == -1 and counter <= k:
            return True

        return False
